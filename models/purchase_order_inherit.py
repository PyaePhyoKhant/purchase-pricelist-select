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
        super call this method first and then set price form purchase pricelist
        """
        if self.product_id:
            # super call method first so that vendor pricelist still works correctly even without purchase pricelist
            super()._onchange_quantity()

            # search by variant first and then if not found by template
            price_list_item = self.order_id.vendor_pl_id.item_ids.filtered(lambda x: x.product_id == self.product_id)
            if not price_list_item:
                price_list_item = self.order_id.vendor_pl_id.item_ids.filtered(lambda x: x.product_tmpl_id == self.product_id.product_tmpl_id)

            if price_list_item:
                self.price_unit = price_list_item.fixed_price
