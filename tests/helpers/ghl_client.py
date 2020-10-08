from typing import Optional

from django.contrib.auth.models import AnonymousUser, User
from graphene.test import Client
from jnt_django_toolbox.helpers.objects import dict2obj

from tests.gql import schema


class GraphQLClient(Client):
    """Test graphql client."""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing."""
        super().__init__(schema, *args, **kwargs)

        self._user: Optional[User] = None

    def set_user(self, user: User) -> None:
        """Set user for auth requests."""
        self._user = user

    def execute(self, *args, **kwargs):
        """Execute graphql request."""
        context = {
            "user": self._user or AnonymousUser(),
        }

        context.update(kwargs.get("extra_context", {}))

        kwargs["context_value"] = dict2obj(context)

        return super().execute(*args, **kwargs)
