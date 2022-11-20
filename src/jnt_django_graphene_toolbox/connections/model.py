from graphene import Connection, Int
from graphql import GraphQLResolveInfo


class ModelConnection(Connection):
    """Datasource connection."""

    class Meta:
        """Meta."""

        abstract = True

    count = Int()

    def resolve_count(self, info: GraphQLResolveInfo):  # noqa: WPS110
        """Resolve collection length."""
        return self.length
