import graphene
from graphene.utils.str_converters import to_snake_case


class BitField(graphene.List):
    """Bit field."""

    def __init__(self, enum, *args, **kwargs):
        self._resolver = kwargs.get("resolver")
        kwargs["resolver"] = self._resolver_wrap
        super().__init__(graphene.Enum.from_enum(enum), *args, **kwargs)

    def _resolver_wrap(self, instance, info):
        if self._resolver:
            values = self._resolver(instance, info)
        else:
            values = getattr(instance, to_snake_case(info.field_name))

        return [key for key, setted in values if setted]
