from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_pl_id = fields.Many2one('purchase.pricelist', 'Pricelist')


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_qty', 'product_uom')
    def _onchange_quantity(self):
        """
        `_onchange_quantity` method set unit price
        super call this method first and set price form purchase pricelist
        """
        super()._onchange_quantity()
