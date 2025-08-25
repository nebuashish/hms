# -*- coding: utf-8 -*-
# Part of AlmightyCS. See LICENSE file for full copyright and licensing details.
#╔══════════════════════════════════════════════════════════════════════╗
#║                                                                      ║
#║                  ╔═══╦╗       ╔╗  ╔╗     ╔═══╦═══╗                   ║
#║                  ║╔═╗║║       ║║ ╔╝╚╗    ║╔═╗║╔═╗║                   ║
#║                  ║║ ║║║╔╗╔╦╦══╣╚═╬╗╔╬╗ ╔╗║║ ╚╣╚══╗                   ║
#║                  ║╚═╝║║║╚╝╠╣╔╗║╔╗║║║║║ ║║║║ ╔╬══╗║                   ║
#║                  ║╔═╗║╚╣║║║║╚╝║║║║║╚╣╚═╝║║╚═╝║╚═╝║                   ║
#║                  ╚╝ ╚╩═╩╩╩╩╩═╗╠╝╚╝╚═╩═╗╔╝╚═══╩═══╝                   ║
#║                            ╔═╝║     ╔═╝║                             ║
#║                            ╚══╝     ╚══╝                             ║
#║                  SOFTWARE DEVELOPED AND SUPPORTED BY                 ║
#║                ALMIGHTY CONSULTING SOLUTIONS PVT. LTD.               ║
#║                      COPYRIGHT (C) 2016 - TODAY                      ║
#║                      https://www.almightycs.com                      ║
#║                                                                      ║
#╚══════════════════════════════════════════════════════════════════════╝
{
    'name': 'Hospital Cashier Management',
    'category': 'Medical',
    'summary': 'Hospital Cashier Management',
    'description': """
        Hospital Cashier Management
    """,
    'version': '1.0.4',
    'author': 'Almighty Consulting Solutions Pvt. Ltd.',
    'support': 'info@almightycs.com',
    'website': 'https://www.almightycs.com',
    'license': 'OPL-1',
    'depends': ['acs_hms_hospitalization','acs_hms_vaccination'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/data.xml',

        'views/hms_invoice_view.xml',
        'views/hms_appointment_view.xml',
        'views/hms_hospitalization.xml',
        'views/hms_surgery_view.xml',
        'views/patient_procedure_view.xml',
        'views/hms_vaccination_view.xml',
        'views/res_config_view.xml',
        'views/menu_item.xml',
    ],
    'images': [
        'static/description/acs_hms_cashier_almightycs_cover.jpg',
    ],
    'installable': True,
    'application': True,
    'sequence': 2,
    'price': 99,
    'currency': 'USD',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: