# -*- coding: utf-8 -*-
import os, sys

LOGIN = 'u1659622'
PROJECT_NAME = 'kruiso'
PYTHON = '3.10'
VENV = 'env'

sys.path.insert(0, f'/var/www/{LOGIN}/data/www/{PROJECT_NAME}.ru/{PROJECT_NAME}')
sys.path.insert(1, f'/var/www/{LOGIN}/data/{VENV}/lib/python{PYTHON}/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()