from typing import Dict

from graphene.utils import str_converters
from graphql import GraphQLResolveInfo
from graphql.utilities.ast_to_dict import ast_to_dict


def collect_fields(node, fragments: Dict[str, object]):
    """Collect fields."""
    field = {}

    selection_set = node.get("selection_set")

    if selection_set:
        for leaf in selection_set["selections"]:
            if leaf["kind"] == "Field":
                name = str_converters.to_snake_case(leaf["name"]["value"])
                field[name] = collect_fields(leaf, fragments)
            elif leaf["kind"] == "FragmentSpread":
                field.update(
                    collect_fields(
                        fragments[leaf["name"]["value"]],
                        fragments,
                    ),
                )

    return field


def get_fields_from_info(info: GraphQLResolveInfo):  # noqa: WPS110
    """Get fields from info."""
    fragments = {}
    node = ast_to_dict(info.field_asts[0])  # type:ignore

    for name, fragment_value in info.fragments.items():
        fragments[name] = ast_to_dict(fragment_value)  # type:ignore

    return collect_fields(node, fragments)


def is_field_selected(
    info: GraphQLResolveInfo,  # noqa: WPS110
    path: str,
) -> bool:
    """Is field selected."""
    fields = get_fields_from_info(info)

    for key in path.split("."):
        try:
            fields = fields[key]
        except KeyError:
            return False

    return True
