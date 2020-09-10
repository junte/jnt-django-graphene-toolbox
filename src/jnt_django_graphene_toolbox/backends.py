# -*- coding: utf-8 -*-

from graphql import GraphQLCoreBackend, GraphQLError
from graphql.execution.executors.sync import SyncExecutor


class GraphQLSyncExecutor(SyncExecutor):
    """Executor with GraphQLError catching."""

    def execute(self, fn, *args, **kwargs):
        """
        Execution handler.

        Wraps gql errors for non logging as exceptions.
        """
        try:
            return super().execute(fn, *args, **kwargs)
        except GraphQLError as err:
            return err


class GraphQLBackend(GraphQLCoreBackend):
    """GraphQL backend."""

    def __init__(self, executor=None):
        """Initializing."""
        if not executor:
            executor = GraphQLSyncExecutor()
        super().__init__(executor)
