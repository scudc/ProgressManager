import os
import sys
import django.core.handlers.wsgi

sys.path.append("F:/hobodong/ProgressManager")
os.environ['DJANGO_SETTINGS_MODULE'] = 'restApi.settings'

application = django.core.handlers.wsgi.WSGIHandler()