

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CollectionsDetailResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the node entity.
    """

    collected_metadata: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of metadata entries that are linked to the current collections.
    """

    linked_nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are linked to the current collection.
    """

    linked_preprints: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of preprints that are linked to the current collection.
    """

    linked_registrations: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of registrations that are linked to the current collection.
    """

    node_links: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are linked to the current collection.
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of preprints that this node relates to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
