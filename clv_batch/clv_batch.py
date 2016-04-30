# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields
from datetime import *


class Batch(models.Model):
    _name = "clv_batch"

    name = fields.Char('Batch', required=True, size=128, translate=False)
    alias = fields.Char('Alias', size=128, help='Common name that the batch is referred')
    code = fields.Char(size=64, string='Batch Code', required=False)
    description = fields.Char(string='Description', size=256)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the batch without removing it.",
                            default=1)
    origin_batch_ids = fields.Many2many(
        'clv_batch',
        'clv_batch_origin_rel',
        'to_batch_id',
        'from_batch_id',
        'Origin Batches'
    )
    derived_batch_ids = fields.Many2many(
        'clv_batch',
        'clv_batch_origin_rel',
        'from_batch_id',
        'to_batch_id',
        'Derived Batches'
    )

    _order = 'name'

    _sql_constraints = [
        ('uniq_code', 'unique(code)', "Error! The Batch Code must be unique!"),
    ]
