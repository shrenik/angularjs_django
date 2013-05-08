#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf import settings
from django.conf.urls import include, patterns
from app.urls import urlpatterns as urlpatterns_app
from django.contrib import admin
import os

try:
    admin.autodiscover()
except admin.sites.AlreadyRegistered:
    # nose imports the admin.py files during tests, so
    # the models have already been registered.
    pass


js_info_dict = {
    'domain': 'djangojs',
    'packages': ('dialer_campaign',
                 'user_profile',
                 'survey',
                 'audiofield'),
}

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += urlpatterns_app


urlpatterns += patterns('',
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip(os.sep),
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
