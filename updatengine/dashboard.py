###################################################################################
# UpdatEngine - Software Packages Deployment and Administration tool              #  
#                                                                                 #
# Copyright (C) Yves Guimard - yves.guimard@gmail.com                             #
#                                                                                 #
# This program is free software; you can redistribute it and/or                   #
# modify it under the terms of the GNU General Public License                     #
# as published by the Free Software Foundation; either version 2                  #
# of the License, or (at your option) any later version.                          #
#                                                                                 #
# This program is distributed in the hope that it will be useful,                 #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                  #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                   #
# GNU General Public License for more details.                                    #
#                                                                                 #
# You should have received a copy of the GNU General Public License               #
# along with this program; if not, write to the Free Software                     #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA. #
###################################################################################

"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'updatengine.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """


    def init_with_context(self, context):

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
		title='',
		collapsible=False,
		column=1,
		css_classes=('collapse closed',),
		models=('inventory.*',)
		))
	self.children.append(modules.AppList(
		title='',
		title_url='',
		collapsible=False,
		column=1,
		css_classes=('collapse closed',),
		models=('deploy.*',)
		))
	self.children.append(modules.AppList(
		title='',
		title_url='',
		collapsible=False,
		column=2,
		css_classes=('collapse closed',),
		models=('configuration.*',)
		))


        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('ModelList: Administration'),
            column=2,
            collapsible=False,
            models=('django.contrib.*',),
        ))

	# UpdatEngine feed module. Uncomment to show on dashboard
#	self.children.append(modules.Feed(
#		_('ModelList: Latest News'),
#		column=2,
#		collapsible=False,
#		feed_url='http://www.updatengine.com/?feed=rss2',
#		limit=3
#	))


	self.children.append(modules.LinkList(
		_('ModelList: Links'),
		layout='inline',
		column=2,
            	collapsible=False,
		children=(
			['www.updatengine.com', 'http://www.updatengine.com', True],
			['Rss updatengine.com', 'http://www.updatengine.com/?feed=rss2', True],
		)
	))
