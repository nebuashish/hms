from odoo import models, fields, api
import requests
import json
import time
import base64
import io
import tempfile
import logging
_logger = logging.getLogger(__name__)


class HMSOCR(models.Model):
    _name = 'hms.ocr'
    _description = 'HMS OCR Processing'
    
    # Binary field to store the file
    handwritten_file = fields.Binary(
        string='Handwritten Document',
        help='Upload the handwritten document for OCR processing'
    )
    
    # Character field to store filename
    filename = fields.Char(
        string='Filename',
        help='Name of the uploaded file'
    )
    
    # Field to store OCR results
    ocr_results = fields.Text(
        string='OCR Results',
        readonly=True,
        help='Extracted text from handwritten document'
    )
    
    # Status field
    processing_status = fields.Selection([
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], string='Processing Status', default='pending')

    @api.model
    def create(self, vals):
        """Override create to automatically process OCR when record is created"""
        # Create the record first
        record = super(HMSOCR, self).create(vals)
        
        # If a handwritten file is uploaded, process OCR automatically
        if record.handwritten_file:
            record._process_ocr_on_create()
        
        return record

    def _process_ocr_on_create(self):
        """Process OCR automatically on record creation"""
        if not self.handwritten_file:
            return
        
        # Initialize OCR client
        api_token = "967|avEpQRGRyokc5LiQPpDGrcPqzZ1QZQ3h9m4vejoD4efc9b6d"
        ocr = HandwritingOCR(api_token)
        
        try:
            # Update status to processing
            self.processing_status = 'processing'
            
            # Process handwriting from binary data
            results = ocr.process_handwriting_from_binary(
                self.handwritten_file,
                self.filename or 'document.jpg'
            )
            
            # Format results
            formatted_results = ""
            for result in results:
                formatted_results += f"Page {result['page']}:\n"
                formatted_results += result['text']
                formatted_results += "\n" + "-" * 50 + "\n"
            
            # Update the record with results
            self.ocr_results = formatted_results
            self.processing_status = 'completed'
            
            _logger.info(f"OCR processing completed for record {self.id}")
            
        except Exception as e:
            self.processing_status = 'failed'
            self.ocr_results = f'Auto-processing failed: {str(e)}'
            _logger.error(f"OCR processing failed for record {self.id}: {str(e)}")


class HandwritingOCR:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://www.handwritingocr.com/api/v3"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/json"
        }
    
    def upload_document_from_binary(self, binary_data, filename, action="transcribe"):
        """Upload document from binary data for OCR processing"""
        url = f"{self.base_url}/documents"
        
        # Create a file-like object from binary data
        file_obj = io.BytesIO(base64.b64decode(binary_data))
        
        files = {'file': (filename, file_obj, 'application/octet-stream')}
        data = {'action': action}
        
        response = requests.post(url, headers=self.headers, files=files, data=data)
        response.raise_for_status()
        
        return response.json()
    
    def get_document_status(self, document_id):
        """Check document processing status"""
        url = f"{self.base_url}/documents/{document_id}"
        
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        return response.json()
    
    def get_document_result(self, document_id):
        """Get OCR results for processed document"""
        url = f"{self.base_url}/documents/{document_id}"
        
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        return response.json()
    
    def process_handwriting_from_binary(self, binary_data, filename, timeout=120):
        """Complete workflow: upload from binary data, wait for processing, return results"""
        upload_response = self.upload_document_from_binary(binary_data, filename)
        document_id = upload_response['id']
        
        # Poll for completion
        start_time = time.time()
        while time.time() - start_time < timeout:
            status_response = self.get_document_status(document_id)
            status = status_response['status']
            
            if status == "processed":
                result = self.get_document_result(document_id)
                return self.extract_text(result)
            elif status == "failed":
                raise Exception("Document processing failed")
            
            time.sleep(2)
        
        raise Exception("Processing timeout exceeded")
    
    def extract_text(self, result):
        """Extract text from API response"""
        extracted_text = []
        
        if 'results' in result:
            for page_result in result['results']:
                page_num = page_result['page_number']
                transcript = page_result['transcript']
                extracted_text.append({
                    'page': page_num,
                    'text': transcript
                })
        
        return extracted_text


