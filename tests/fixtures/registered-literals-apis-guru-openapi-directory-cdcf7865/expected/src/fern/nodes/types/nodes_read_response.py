

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_read_response_attributes import NodesReadResponseAttributes
from .nodes_read_response_links import NodesReadResponseLinks
from .nodes_read_response_relationships import NodesReadResponseRelationships


class NodesReadResponse(UniversalBaseModel):
    attributes: NodesReadResponseAttributes = pydantic.Field()
    """
    The properties of the node entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the node entity.
    """

    links: typing.Optional[NodesReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the node entity.
    """

    relationships: typing.Optional[NodesReadResponseRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the node entity.
    """

    type: str = pydantic.Field()
    """
    The type identifier of the node entity (`nodes`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
