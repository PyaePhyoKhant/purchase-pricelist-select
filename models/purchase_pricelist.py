from odoo import api, fields, models


class PurchasePricelist(models.Model):
    _name = 'purchase.pricelist'
    _inherit = 'product.pricelist'

    country_group_ids = fields.Many2many('res.country.group', 'res_country_group_purchase_pricelist_rel',
                                         'purchase_pricelist_id', 'res_country_group_id', string='Country Groups')
