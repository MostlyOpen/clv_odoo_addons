# -*- coding: utf-8 -*-
###############################################################################
#
# For copyright and license notices, see __openerp__.py file in root directory
#
###############################################################################

from openerp import models, fields


class Person(models.Model):
    _inherit = 'clv_person'

    is_patient = fields.Boolean('Is Patient',
                                help="If checked, the Person is a Patient.",
                                default=0)
