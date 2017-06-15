# -*- coding: utf-8 -*-
#
#
#    Copyright 2015 Camptocamp SA
#    Author: Alexandre Fayolle
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
{'name': 'NGO - Purchase Requisition',
 'summary': 'Base Purchase Requisition view for NGO',
 'version': '10.0.1.0.0',
 'author': 'Camptocamp,Odoo Community Association (OCA),\
         Serpent Consulting Services Pvt. Ltd.',
 'license': 'AGPL-3',
 'category': 'Purchase Management',
 'complexity': 'normal',
 'website': 'http://www.camptocamp.com',
 'depends': ['purchase_requisition',
             'purchase_requisition_bid_selection',
             'purchase_requisition_delivery_address',
             'purchase_requisition_auto_rfq',
             'purchase_requisition_transport_document',
             ],
 'data': ['view/purchase_order.xml',
          'view/purchase_requisition.xml',
          ],
 'installable': True,
 'auto_install': False,
}
