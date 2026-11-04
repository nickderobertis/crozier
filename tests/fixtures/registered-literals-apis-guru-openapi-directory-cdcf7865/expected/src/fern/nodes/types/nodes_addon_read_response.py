

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_addon_read_response_attributes import NodesAddonReadResponseAttributes
from .nodes_addon_read_response_links import NodesAddonReadResponseLinks


class NodesAddonReadResponse(UniversalBaseModel):
    attributes: typing.Optional[NodesAddonReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the node addon entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the draft registration entity.
    """

    links: typing.Optional[NodesAddonReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the node addon entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the node addon entity (`node_addons`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
