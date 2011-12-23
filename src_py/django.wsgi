import os
import sys


path = '/home/ubuntu/django_projects/libras'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'libras.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
