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
    'name': 'Patient',
    'summary': 'Patient Module used in CLVsol Solutions.',
    'version': '2.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'images': [],
    'depends': [
        # 'clv_base',
        # 'clv_tag',
        # 'clv_annotation',
        'clv_person',
        # 'clv_family',
        # 'clv_community',
        ],
    'data': [
        'security/clv_patient_security.xml',
        # 'security/ir.model.access.csv',
        # 'clv_patient_view.xml',
        'clv_person_view.xml',
        # 'category/clv_patient_category_view.xml',
        # 'address/clv_address_view.xml',
        # 'tag/clv_tag_view.xml',
        # 'annotation/clv_annotation_view.xml',
        # # 'seq/clv_patient_sequence.xml',
        # # 'seq/clv_patient_category_sequence.xml',
        # # 'wkf/clv_patient_workflow.xml',
        # # 'wkf/clv_patient_wkf_view.xml',
        # # 'history/clv_patient_history_view.xml',
        # # 'clv_family_member/clv_family_member_view.xml',
        # # 'clv_community_member/clv_community_member_view.xml',
        'menu/clv_patient_menu_view.xml',
        # # 'clv_address/clv_address_view.xml',
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
