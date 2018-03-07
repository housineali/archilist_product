# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, RedirectWarning, except_orm
from datetime import datetime


class Product(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    @api.one
    @api.depends('categ_id')
    def _compute_is_interior(self):
        for item in self.categ_id:
            if item.type == 'interior':
                self.interior = True
                break

    @api.one
    @api.depends('categ_id')
    def _compute_is_exterior(self):
        for item in self.categ_id:
            if item.type == 'exterior':
                self.exterior = True
                break

    @api.one
    @api.depends('categ_id')
    def _compute_is_outdoor(self):
        for item in self.categ_id:
            if item.type == 'landscape_and_outdoor':
                self.outdoor = True
                break

    def _get_default_category_id(self):
        if self._context.get('categ_id') or self._context.get('default_categ_id'):
            return self._context.get('categ_id') or self._context.get('default_categ_id')
        category = self.env.ref('product.product_category_all', raise_if_not_found=False)
        if not category:
            category = self.env['product.category'].search([], limit=1)
        if category:
            return category
        else:
            err_msg = _('You must define at least one product category in order to be able to create products.')
            redir_msg = _('Go to Internal Categories')
            raise RedirectWarning(err_msg, self.env.ref('product.product_category_action_form').id, redir_msg)

    categ_id = fields.Many2many(
        comodel_name='product.category', string='Internal Category',
        change_default=True, default=_get_default_category_id,
        required=True, help="Select category for the current product")
    type = fields.Selection(
        selection_add=[('product', 'Stockable Product'), ('package', 'Package(Service & Stockable)')])
    interior = fields.Boolean(string="", compute=_compute_is_interior, store=True)
    exterior = fields.Boolean(string="", compute=_compute_is_exterior, store=True)
    outdoor = fields.Boolean(string="", compute=_compute_is_outdoor, store=True)
    contractor_id = fields.Many2one(comodel_name="res.users", string="", required=False, )


    @api.model
    def create(self,vals):
        vals['contractor_id']=self.env.uid
        res = super(Product, self).create(vals)
        return res



class ProductCategory(models.Model):
    _name = "product.category"
    _inherit = "product.category"

    @api.one
    def _compute_all_product_ids(self):
        products= self.env['product.product'].search([])
        ids=[]
        for product in products:
            if self.id in product.categ_id.mapped('id'):
                ids.append(product.id)
        self.all_product_ids=self.env['product.product'].search([('id','in',ids)])


    type = fields.Selection(string="Type", selection=[('interior', 'Interior'), ('exterior', 'Exterior'),
                                                  ('landscape_and_outdoor', 'Landscape & Outdoor'), ],
                            default='interior', required=False, )
    uom_id = fields.Many2one(comodel_name="product.uom", string="Unit Of Measure", required=False, )
    product_ids = fields.Many2many(comodel_name="product.product", relation="categ_product_rel", string="Products", )
    all_product_ids = fields.Many2many(comodel_name="product.product", relation="all_categ_product_rel", compute=_compute_all_product_ids,string="Products", store=False)
