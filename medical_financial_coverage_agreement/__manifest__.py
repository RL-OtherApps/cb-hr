# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Financial Coverage Agreement',
    'version': '11.0.1.0.0',
    'author': "Eficent, Creu Blanca, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_financial_coverage',
        'medical_administration_location',
        'product',
        'medical_workflow',
        'sale',
    ],
    'website': 'https://github.com/OCA/vertical-medical',
    "license": "LGPL-3",
    "data": [
        'views/medical_coverage_agreement_item_view.xml',
        'views/medical_coverage_agreement_view.xml',
        'views/medical_coverage_template_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'test': [

    ],
    'installable': True,
    'auto_install': False,
}