# -*- coding: utf-8 -*-

from graphql import GraphQLCoreBackend
from graphql.execution.executors.sync import SyncExecutor

from jnt_django_graphene_toolbox.errors.base import BaseGraphQLError


class GraphQLSyncExecutor(SyncExecutor):
    """Executor with GraphQLError catching."""

    def execute(self, fn, *args, **kwargs):
        """Execution handler."""
        try:
            return super().execute(fn, *args, **kwargs)
        except BaseGraphQLError as err:
            return err


class GraphQLBackend(GraphQLCoreBackend):
    """GraphQL backend."""

    def __init__(self, executor=None):
        """Initializing."""
        if not executor:
            executor = GraphQLSyncExecutor()
        super().__init__(executor)
