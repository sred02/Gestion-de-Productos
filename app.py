import os
import sys

# Agregar la carpeta uniweb2 al path para que Django encuentre sus módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'uniweb2'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uniweb2.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
