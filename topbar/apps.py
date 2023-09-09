from django.apps import AppConfig


class TopbarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topbar'
    
    def ready(self):
        from . import signals
        return signals 
