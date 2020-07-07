# -*- coding: utf-8 -*-

from django.conf import settings


def pytest_configure(config):
    """Build test app settings."""
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            },
        },
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "graphene_django",
            "jnt_django_toolbox",
            "tests",
        ],
        ROOT_URLCONF="",
        DEBUG=False,
    )


pytest_plugins = (
    "tests.fixtures.ghl",
    "tests.fixtures.requests",
    "tests.fixtures.users",
)
