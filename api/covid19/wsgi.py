"""
WSGI config for covid19 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

# if .env file exists on api dir, read it
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    dotenv.read_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covid19.settings')

application = get_wsgi_application()
