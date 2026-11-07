

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_identifiers_list_response_item_attributes import NodesIdentifiersListResponseItemAttributes
from .nodes_identifiers_list_response_item_links import NodesIdentifiersListResponseItemLinks
from .nodes_identifiers_list_response_item_relationships import NodesIdentifiersListResponseItemRelationships


class NodesIdentifiersListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[NodesIdentifiersListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the identifier entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the identifier entity.
    """

    links: typing.Optional[NodesIdentifiersListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the identifier entity.
    """

    relationships: typing.Optional[NodesIdentifiersListResponseItemRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the identifier entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the identifier entity (`identifiers`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
