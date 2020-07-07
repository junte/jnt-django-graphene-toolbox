# -*- coding: utf-8 -*-

import pytest
from graphql import ResolveInfo


def _get_mock_info(request) -> ResolveInfo:
    from graphene_django.rest_framework.tests import (  # noqa: WPS433
        test_mutation,
    )

    mock_info = test_mutation.mock_info()
    mock_info.context = request
    mock_info.field_asts = [{}]
    mock_info.fragments = {}
    return mock_info


@pytest.fixture()
def ghl_mock_info(rf) -> ResolveInfo:
    """Provides graphql mocked info."""
    request = rf.get("/graphql/")

    return _get_mock_info(request)


@pytest.fixture()
def ghl_auth_mock_info(user, auth_rf) -> ResolveInfo:
    """Provides graphql mocked info with auth user."""
    request = auth_rf.get("/graphql/")

    return _get_mock_info(request)
