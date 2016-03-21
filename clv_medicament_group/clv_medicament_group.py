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
from datetime import datetime


class MedicamentGroup(models.Model):
    _name = 'clv_medicament_group'

    name = fields.Char('Name', size=256, select=1, required=True, help='Medicament Group Name')
    alias = fields.Char('Alias', size=64, help='Common name that the Medicament Group is referred')
    code = fields.Char(size=64, string='Medicament Group Code', required=False)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the medicament group without removing it.",
                            default=1)
    medicament_name = fields.Char(size=256, string='Medicament Name')
    concentration = fields.Char(size=256, string='Concentration')
    pres_form = fields.Many2one('clv_medicament.form', string='Presentation Form',
                                help='Medicament form, such as tablet or gel')

    _order = 'name'


class MedicamentGroup_2(models.Model):
    _inherit = 'clv_medicament_group'

    active_component = fields.Many2one('clv_medicament.active_component',
                                       string='Active Component',
                                       help='Medicament Active Component')
    active_component_name = fields.Char(related='active_component.name',
                                        string='Related Active Component')
