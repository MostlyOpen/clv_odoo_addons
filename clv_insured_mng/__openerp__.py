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

{
    'name': 'Insured Management',
    'summary': 'Insured Management Module used in CLVsol Solutions.',
    'version': '2.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'images': [],
    'depends': [
        'clv_base',
        # 'clv_tag',
        # 'clv_annotation',
        # 'clv_address',
        # 'clv_insured',
        # 'clv_insured_card',
        ],
    'data': [
        'security/clv_insured_mng_security.xml',
        'security/ir.model.access.csv',
        'clv_insured_mng_view.xml',
        # 'category/clv_insured_category_view.xml',
        # 'tag/clv_tag_view.xml',
        # 'annotation/clv_annotation_view.xml',
        # 'wkf/clv_insured_mng_workflow.xml',
        # 'wkf/clv_insured_mng_wkf_view.xml',
        # 'history/clv_insured_mng_history_view.xml',
        'menu/clv_insured_mng_menu_view.xml',
        # 'insurance/clv_insurance_view.xml',
        # 'insurance_client/clv_insurance_client_view.xml',
        # 'role/clv_insured_view.xml',
        # 'address/clv_insured_mng_view.xml',
        # 'insured_card/clv_insured_mng_view.xml',
        # 'relation/clv_insured_mng_relation_view.xml',
        ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
