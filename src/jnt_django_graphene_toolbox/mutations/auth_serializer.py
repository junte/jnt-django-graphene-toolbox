from jnt_django_graphene_toolbox.mutations import SerializerMutation
from jnt_django_graphene_toolbox.security.mixins.mutation import AuthMutation


class AuthSerializerMutation(AuthMutation, SerializerMutation):
    """Serializer mutation with authorization support."""

    class Meta:
        abstract = True

    @classmethod
    def internal_mutate(
        cls, root, info, **kwargs,  # noqa: WPS110
    ) -> "SerializerMutation":
        """Overrided mutate handler with permissions check."""
        cls.check_premissions(root, info, **kwargs)
        return super().internal_mutate(root, info, **kwargs)
