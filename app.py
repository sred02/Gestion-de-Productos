import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
DJANGO_DIR = os.path.join(BASE, 'uniweb2')
sys.path.insert(0, DJANGO_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'uniweb2.settings'

# Correr collectstatic al iniciar si staticfiles está vacío
import django
django.setup()

from django.core.management import call_command
staticfiles_dir = os.path.join(DJANGO_DIR, 'staticfiles')
if not os.path.exists(staticfiles_dir) or not os.listdir(staticfiles_dir):
    call_command('collectstatic', '--noinput', verbosity=0)

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
