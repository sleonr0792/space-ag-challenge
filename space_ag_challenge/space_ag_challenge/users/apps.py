from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "space_ag_challenge.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import space_ag_challenge.users.signals  # noqa F401
        except ImportError:
            pass
