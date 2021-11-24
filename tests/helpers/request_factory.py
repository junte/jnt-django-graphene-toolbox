from typing import TYPE_CHECKING, Optional

from django.http import HttpRequest
from django.test.client import RequestFactory as DjangoRequestFactory

if TYPE_CHECKING:
    from django.contrib.auth.models import User  # noqa: WPS433


class _MockStorageMessages:
    def add(self, level, message, extra_tags):
        """Mocked add."""


class RequestFactory(DjangoRequestFactory):
    """Request factory for testing requests."""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing."""
        super().__init__(*args, **kwargs)

        self._user: Optional["User"] = None

    def set_user(self, user) -> None:  # noqa: WPS615
        """Set user for auth requests."""
        self._user = user

    def get(self, *args, **kwargs):
        """Construct a GET request."""
        request = super().get(*args, **kwargs)
        self._auth_if_need(request)

        return request

    def post(self, *args, **kwargs):
        """Construct a POST request."""
        request = super().post(*args, **kwargs)
        request._dont_enforce_csrf_checks = True  # noqa: WPS437
        request._messages = _MockStorageMessages()  # noqa: WPS437
        self._auth_if_need(request)

        return request

    def _auth_if_need(self, request: HttpRequest) -> None:
        from django.contrib.auth.models import AnonymousUser  # noqa: WPS433

        request.user = self._user or AnonymousUser()
