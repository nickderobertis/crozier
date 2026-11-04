

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_providers_read_response_attributes import NodesProvidersReadResponseAttributes
from .nodes_providers_read_response_links import NodesProvidersReadResponseLinks
from .nodes_providers_read_response_relationships import NodesProvidersReadResponseRelationships


class NodesProvidersReadResponse(UniversalBaseModel):
    attributes: typing.Optional[NodesProvidersReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the file entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the file entity.
    """

    links: typing.Optional[NodesProvidersReadResponseLinks] = pydantic.Field(default=None)
    """
    Links to alternative representations of the file entity.
    """

    relationships: typing.Optional[NodesProvidersReadResponseRelationships] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the file entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the file entity (`files`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
