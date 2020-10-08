import pytest

from tests.helpers.request_factory import RequestFactory


@pytest.fixture()
def rf() -> RequestFactory:
    """Request factory."""
    return RequestFactory()


@pytest.fixture()
def auth_rf(rf, user) -> RequestFactory:
    """Request factory with setted user."""
    rf.set_user(user)

    return rf
