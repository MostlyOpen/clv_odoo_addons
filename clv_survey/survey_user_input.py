# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import models, fields


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    external_code = fields.Char('External Code', size=128, help="External Code")
