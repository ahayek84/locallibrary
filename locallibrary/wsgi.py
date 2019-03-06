"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
#import sys
#sys.path = ['C:\wamp64\www\django_projects\locallibrary\locallibrary'] + sys.bath

from django.core.wsgi import get_wsgi_application

from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

application = get_wsgi_application()
