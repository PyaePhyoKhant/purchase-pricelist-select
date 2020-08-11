from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_pl_id = fields.Many2one('product.supplierinfo', 'Pricelist')
