from django.apps import AppConfig


class CartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'

    # will cause tests failure.
    # uncomment when not testing.
    # def ready(self):
        # import carts.receivers