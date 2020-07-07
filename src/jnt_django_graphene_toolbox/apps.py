# -*- coding: utf-8 -*-

from django.apps import AppConfig as DjangoAppConfig
from jnt_django_toolbox.helpers.modules import load_module_from_app


class AppConfig(DjangoAppConfig):
    """Application entry config."""

    name = "jnt_django_graphene_toolbox"
    verbose_name = "Django graphene toolbox"

    def ready(self):
        """Run this code when Django starts."""
        super().ready()

        load_module_from_app(self, "fields")
        load_module_from_app(self, "converters.models")
        load_module_from_app(self, "converters.serializers")
