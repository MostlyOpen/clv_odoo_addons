# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2016-Today  Carlos Eduardo Vercelino - CLVsol
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
from openerp import exceptions

import logging
_logger = logging.getLogger(__name__)


class TodoWizard(models.TransientModel):
    _name = 'clv_todo.wizard'
    task_ids = fields.Many2many('clv_todo.task', string='Tasks')
    new_user_id = fields.Many2one('res.users', string='Set Responsible')
    new_deadline = fields.Date('Set Deadline')

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        if not (self.new_deadline or self.new_user_id):
            raise exceptions.ValidationError('No data to update!')
        # else:
        _logger.debug('Mass update on Todo Tasks %s',
                      self.task_ids.ids)
        if self.new_deadline:
            self.task_ids.write({'date_deadline': self.new_deadline})
        if self.new_user_id:
            self.task_ids.write({'user_id': self.new_user_id.id})
        return True

    @api.multi
    def do_count_tasks(self):
        Task = self.env['clv_todo.task']
        count = Task.search_count([])
        raise exceptions.Warning(
            'There are %d active tasks.' % count)

    @api.multi
    def do_reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'}

    @api.multi
    def do_populate_tasks(self):
        self.ensure_one()
        Task = self.env['clv_todo.task']
        all_tasks = Task.search([])
        self.task_ids = all_tasks
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
