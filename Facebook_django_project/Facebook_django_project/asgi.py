"""
ASGI config for Facebook_django_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
# Web Server Gateway Interface (WSGI)
# ASGI (Asynchronous Server Gateway Interface)


# Run command in Terminal ==  daphne Facebook_django_project.asgi:application
import os
import django

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Facebook_django_project.settings')
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

from core.routing import websocket_urlpatterns


application = ProtocolTypeRouter({

    'http': get_asgi_application(),

    'https': get_asgi_application(),

    'websocket': AuthMiddlewareStack(

        URLRouter(

            websocket_urlpatterns

        )

    )

})

# TODO: CREATE Client side