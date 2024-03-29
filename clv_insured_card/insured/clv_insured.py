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


class InsuredCard(models.Model):
    _inherit = 'clv_insured_card'

    insured_id = fields.Many2one('clv_insured', 'Insured')
    insured_code = fields.Char('Insured Code', related='insured_id.code')
    insured_birthday = fields.Date('Insured Date of Birth', related='insured_id.birthday')
    insured_age = fields.Char('Insured Age', related='insured_id.age')


class Insured(models.Model):
    _inherit = 'clv_insured'

    insured_card_ids = fields.One2many('clv_insured_card',
                                       'insured_id',
                                       'Insured Cards')
