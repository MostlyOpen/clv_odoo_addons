# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from openerp import models, fields
# from openerp.osv import fields, osv
from datetime import datetime
import math


def ean_checksum(eancode):
    '''returns the checksum of an ean string of length 13, returns -1 if the string has the wrong length'''
    if len(eancode) != 13:
        return -1
    oddsum = 0
    evensum = 0
    total = 0
    eanvalue = eancode
    reversevalue = eanvalue[::-1]
    finalean = reversevalue[1:]

    for i in range(len(finalean)):
        if i % 2 == 0:
            oddsum += int(finalean[i])
        else:
            evensum += int(finalean[i])
    total = (oddsum * 3) + evensum

    check = int(10 - math.ceil(total % 10.0)) % 10
    return check


def check_ean(eancode):
    '''returns True if eancode is a valid ean13 string, or null'''
    if not eancode:
        return True
    if len(eancode) != 13:
        return False
    try:
        int(eancode)
    except:
        return False
    return ean_checksum(eancode) == int(eancode[-1])


class MedicamentModel(models.Model):
    _name = 'clv_medicament.model'

    name = fields.Char('Product Name', select=True, required=True)
    ean13 = fields.Char('EAN13 Barcode', size=13,
                        help="International Article Number used for product identification.")
    code = fields.Char(size=64, string='Medicament Code', required=False)
    medicament_name = fields.Char(size=256, string='Medicament Name')
    concentration = fields.Char(size=256, string='Concentration')
    presentation = fields.Char(size=256, string='Presentation')
    pres_form = fields.Many2one('clv_medicament.form', string='Presentation Form',
                                help='Medicament form, such as tablet or gel')
    pres_quantity = fields.Float(string='Presentation Quantity')
    pres_quantity_unit = fields.Many2one('clv_medicament.uom', string='Quantity Unit',
                                         help='Unit of measure for the medicament to be taken')
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False)
    active = fields.Boolean('Active',
                            help="The active field allows you to hide the medicament without removing it.")
    is_product = fields.Boolean('Is a Product',
                                help="Check if the medicament is a product.")
    is_fraction = fields.Boolean('Is a Fraction',
                                 help="Check if the medicament is a fraction of a product.")

    _order = 'name'

    _sql_constraints = [
        ('name_uniq', 'unique(name)', u'Error! The Medicament Name must be unique!'),
        ('code_uniq', 'unique(code)', u'Error! The Medicament Code must be unique!'),
        ]

    _defaults = {
        'active': 1,
        'is_product': False,
        'is_fraction': False,
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

    def _check_ean_key(self, cr, uid, ids, context=None):
        for medicament in self.read(cr, uid, ids, ['ean13'], context=context):
            if not check_ean(medicament['ean13']):
                return False
        return True

    _constraints = [(_check_ean_key,
                     'You provided an invalid "EAN13 Barcode" reference. ' +
                     'You may use the "Internal Reference" field instead.',
                     ['ean13'])]
