from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WorkerConfig(AppConfig):
    name = "worker"
    verbose_name = _("Worker")
