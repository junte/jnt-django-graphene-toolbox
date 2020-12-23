import graphene


class BaseMutation(graphene.Mutation):
    """A base class mutation."""

    class Meta:
        abstract = True

    @classmethod
    def mutate(cls, root, info, **kwargs):  # noqa: WPS110
        """Mutate."""
        return cls.do_mutate(root, info, **kwargs)

    @classmethod
    def do_mutate(cls, root, info, **kwargs) -> None:  # noqa: WPS110
        """Method should be implemente in subclasses."""
        raise NotImplementedError
