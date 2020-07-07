# -*- coding: utf-8 -*-

import graphene
from graphene_django.debug import DjangoDebug


class Query(graphene.ObjectType):  # noqa: WPS215
    """Class representing all available queries."""

    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(graphene.ObjectType):  # noqa: WPS215
    """Class representing all available mutations."""


schema = graphene.Schema(query=Query, mutation=Mutation)
