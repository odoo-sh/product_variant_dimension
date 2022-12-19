# -*- coding: utf-8 -*-
# Copyright 2022 Sodexis
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    dimensions_length = fields.Float('Length', compute='_compute_dimensions_length', inverse='_set_dimensions_length', store=True)
    dimensions_width = fields.Float('Width', compute='_compute_dimensions_width', inverse='_set_dimensions_width', store=True)
    dimensions_height = fields.Float('Height', compute='_compute_dimensions_height', inverse='_set_dimensions_height', store=True)
    dimensions_uom_id = fields.Many2one('uom.uom', 'Dimensions UOM')

    @api.depends('product_variant_ids', 'product_variant_ids.dimensions_length')
    def _compute_dimensions_length(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.dimensions_length = template.product_variant_ids.dimensions_length
        for template in (self - unique_variants):
            template.dimensions_length = 0.0

    def _set_dimensions_length(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.dimensions_length = template.dimensions_length

    @api.depends('product_variant_ids', 'product_variant_ids.dimensions_width')
    def _compute_dimensions_width(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.dimensions_width = template.product_variant_ids.dimensions_width
        for template in (self - unique_variants):
            template.dimensions_width = 0.0

    def _set_dimensions_width(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.dimensions_width = template.dimensions_width

    @api.depends('product_variant_ids', 'product_variant_ids.dimensions_height')
    def _compute_dimensions_height(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.dimensions_height = template.product_variant_ids.dimensions_height
        for template in (self - unique_variants):
            template.dimensions_height = 0.0

    def _set_dimensions_height(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.dimensions_height = template.dimensions_height

    @api.model
    def create(self, values):
        result = super(ProductTemplate, self).create(values)
        related_values = {}
        related_fields = ['dimensions_length', 'dimensions_width', 'dimensions_height']
        for field in related_fields:
            if values.get(field):
                related_values[field] = values[field]
        if related_values:
            result.write(related_values)
        return result

class ProductProduct(models.Model):
    _inherit = 'product.product'

    dimensions_length = fields.Float('Length')
    dimensions_width = fields.Float('Width')
    dimensions_height = fields.Float('Height')
    dimensions_uom_id = fields.Many2one('uom.uom', 'Dimensions UOM')
