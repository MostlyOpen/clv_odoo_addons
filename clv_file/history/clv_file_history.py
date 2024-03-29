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

from openerp import models, fields, api
from datetime import *


class FileHistory(models.Model):
    _name = 'clv_file.history'

    file_id = fields.Many2one('clv_file', 'File', required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', 'User', required=True)
    date = fields.Datetime("Date", required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('getting', 'Getting'),
        ('stored', 'Stored'),
        ('checked', 'Checked'),
        ('deleted', 'Deleted'),
    ], string='Status', readonly=True)
    notes = fields.Text(string='Notes')

    _order = "date desc"

    _defaults = {
        'user_id': lambda obj, cr, uid, context: uid,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }


class File(models.Model):
    _inherit = 'clv_file'

    history_ids = fields.One2many('clv_file.history', 'file_id', 'File History',
                                  readonly=True)
    active_history = fields.Boolean(
        'Active History',
        help="If unchecked, it will allow you to disable the history without removing it.",
        default=True
    )

    @api.one
    def insert_clv_file_history(self, file_id, state, notes):
        if self.active_history:
            values = {
                'file_id': file_id,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_file.history').create(self._cr, self._uid, values)

    @api.multi
    def write(self, values):
        if ('state' not in values) and ('date_status_change' not in values):
            notes = values.keys()
            self.insert_clv_file_history(self.id, self.state, notes)
        return super(File, self).write(values)

    @api.one
    def button_new(self):
        super(File, self).button_new()
        self.insert_clv_file_history(self.id, 'new', '[state]')

    @api.one
    def button_getting(self):
        super(File, self).button_getting()
        self.insert_clv_file_history(self.id, 'getting', '[state]')

    @api.one
    def button_stored(self):
        super(File, self).button_stored()
        self.insert_clv_file_history(self.id, 'stored', '[state]')

    @api.one
    def button_checked(self):
        super(File, self).button_checked()
        self.insert_clv_file_history(self.id, 'checked', '[state]')

    @api.one
    def button_deleted(self):
        super(File, self).button_deleted()
        self.insert_clv_file_history(self.id, 'deleted', '[state]')
