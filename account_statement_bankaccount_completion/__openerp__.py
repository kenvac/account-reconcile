# -*- coding: utf-8 -*-
#
#
#    Author: Laurent Mignon
#    Copyright 2013 'ACSONE SA/NV'
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{'name': "Bank statement completion from bank account number",
 'version': '9.0.1.0.0',
 'author': "ACSONE SA/NV,Odoo Community Association (OCA)",
 'maintainer': 'ACSONE SA/NV',
 'category': 'Finance',
 'complexity': 'normal',
 'depends': [
     'account_statement_base_import',
 ],
 'website': 'http://www.acsone.eu',
 'data': [
     "data/completion_rule_data.xml",
 ],
 'demo': [],
 'installable': True,
 'auto_install': False,
 'license': 'AGPL-3',
 }
