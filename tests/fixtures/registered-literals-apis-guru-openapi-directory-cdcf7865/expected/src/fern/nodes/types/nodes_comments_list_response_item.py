

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_comments_list_response_item_attributes import NodesCommentsListResponseItemAttributes
from .nodes_comments_list_response_item_links import NodesCommentsListResponseItemLinks
from .nodes_comments_list_response_item_relationships import NodesCommentsListResponseItemRelationships


class NodesCommentsListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[NodesCommentsListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the comment entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the comment entity.
    """

    links: typing.Optional[NodesCommentsListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the comment entity.
    """

    relationships: typing.Optional[NodesCommentsListResponseItemRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the comment entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the comment entity (`comments`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
