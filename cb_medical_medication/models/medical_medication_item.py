from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MedicalMedicationItem(models.Model):
    _name = 'medical.medication.item'

    encounter_id = fields.Many2one(
        'medical.encounter', readonly=True, required=True,
    )
    product_id = fields.Many2one(
        'product.product', required=True,
        domain=[('type', 'in', ['consu', 'product'])],
    )
    location_id = fields.Many2one(
        'res.partner',
        domain=[('stock_location_id', '!=', False),
                ('is_location', '=', True)],
        required=True
    )
    qty = fields.Integer(required=True, default=1)
    price = fields.Float(required=True)
    is_phantom = fields.Integer(default=False)

    @api.onchange('product_id')
    def _onchange_product(self):
        self.price = self.product_id.list_price

    @api.multi
    def _to_medication_request(self):
        requests = self.encounter_id.mapped('careplan_ids').mapped(
            'medication_request_ids'
        ).filtered(
            lambda r: (
                r.product_id == self.product_id.categ_id.category_product_id
                and r.state in ['draft', 'active']
            ))
        # We are adding the information on the first medication request that
        # is not invoicable, that insurance will pay, that private will pay
        for request in requests.filtered(
            lambda r: not r.is_sellable_insurance and not r.is_sellable_private
        ):
            return request._add_medication_item(self)
        for request in requests.filtered(lambda r: r.is_sellable_insurance):
            return request._add_medication_item(self)
        for request in requests.filtered(lambda r: r.is_sellable_private):
            return request._add_medication_item(self)
        # If no medications are found, we are returning an error
        raise ValidationError(_(
            'Request cannot be found for category %s'
        ) % self.product_id.categ_id.display_name)