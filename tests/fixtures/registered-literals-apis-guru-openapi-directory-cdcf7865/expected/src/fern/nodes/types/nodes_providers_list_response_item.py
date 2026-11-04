

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_providers_list_response_item_attributes import NodesProvidersListResponseItemAttributes
from .nodes_providers_list_response_item_links import NodesProvidersListResponseItemLinks
from .nodes_providers_list_response_item_relationships import NodesProvidersListResponseItemRelationships


class NodesProvidersListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[NodesProvidersListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the file entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the file entity.
    """

    links: typing.Optional[NodesProvidersListResponseItemLinks] = pydantic.Field(default=None)
    """
    Links to alternative representations of the file entity.
    """

    relationships: typing.Optional[NodesProvidersListResponseItemRelationships] = pydantic.Field(default=None)
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
