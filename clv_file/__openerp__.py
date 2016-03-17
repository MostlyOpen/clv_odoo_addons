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

{
    'name': 'File',
    'summary': 'File Module used in CLVsol Solutions.',
    'version': '2.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'images': [],
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        ],
    'data': [
        'security/clv_file_security.xml',
        'security/ir.model.access.csv',
        'clv_file_view.xml',
        'category/clv_file_category_view.xml',
        'tag/clv_tag_view.xml',
        'annotation/clv_annotation_view.xml',
        'kanban/clv_file_view.xml',
        'wkf/clv_file_workflow.xml',
        'wkf/clv_file_wkf_view.xml',
        'history/clv_file_history_view.xml',
        'seq/clv_file_seq_view.xml',
        'seq/clv_file_sequence03.xml',
        'seq/clv_file_sequence04.xml',
        'seq/clv_file_sequence06.xml',
        'seq/clv_file_sequence09.xml',
        'seq/clv_file_sequence10.xml',
        'seq/clv_file_category_sequence.xml',
        'menu/clv_file_menu_view.xml',
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
