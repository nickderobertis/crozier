

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_view_only_links_read_response_attributes import NodesViewOnlyLinksReadResponseAttributes
from .nodes_view_only_links_read_response_relationships import NodesViewOnlyLinksReadResponseRelationships


class NodesViewOnlyLinksReadResponse(UniversalBaseModel):
    attributes: typing.Optional[NodesViewOnlyLinksReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the view only link entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the view only link.
    """

    relationships: typing.Optional[NodesViewOnlyLinksReadResponseRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the view only link entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the view only link ('view-only-links').
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
