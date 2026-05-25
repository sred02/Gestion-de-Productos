import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE, 'uniweb2'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'uniweb2.settings'

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
