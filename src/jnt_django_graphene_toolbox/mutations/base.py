import sys
from typing import Optional

import graphene
from graphene.types import mutation
from graphql import ResolveInfo

from jnt_django_graphene_toolbox.errors import (
    BaseGraphQLError,
    GraphQLPermissionDenied,
)


class MutationOptions(mutation.MutationOptions):
    """Base mutation options."""

    permission_classes = None


class BaseMutation(graphene.Mutation):
    """A base class mutation."""

    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(  # noqa: WPS211
        cls,
        permission_classes=None,
        _meta=None,
        **options,
    ):
        """Initialize class with meta."""
        if not _meta:
            _meta = MutationOptions(cls)  # noqa: WPS122

        _meta.permission_classes = permission_classes or []
        super().__init_subclass_with_meta__(_meta=_meta, **options)

    @classmethod
    def mutate(cls, root, info, **kwargs):  # noqa: WPS110
        """Mutate."""
        cls.check_premissions(root, info, **kwargs)

        try:
            return cls.mutate_and_get_payload(root, info)
        except Exception as err:
            payload = cls.handle_error(root, info, err)
            if payload:
                return payload

            raise

    @classmethod
    def check_premissions(
        cls,
        root: Optional[object],
        info: ResolveInfo,  # noqa: WPS110
        **kwargs,  # noqa: WPS125
    ) -> None:
        """Check permissions."""
        has_permission = all(
            perm().has_mutation_permission(root, info, **kwargs)
            for perm in cls._meta.permission_classes
        )

        if not has_permission:
            raise GraphQLPermissionDenied

    @classmethod
    def handle_error(
        cls,
        root: Optional[object],
        info: ResolveInfo,  # noqa: WPS110,
        error: Exception,
    ):
        """Handle error."""
        if isinstance(error, BaseGraphQLError):
            error.stack = sys.exc_info()[2]
            return error

    @classmethod
    def mutate_and_get_payload(
        cls,
        root: Optional[object],
        info: ResolveInfo,  # noqa: WPS110,
        **kwargs,
    ) -> None:  # noqa: WPS110
        """Method should be implemented in subclasses."""
        raise NotImplementedError
