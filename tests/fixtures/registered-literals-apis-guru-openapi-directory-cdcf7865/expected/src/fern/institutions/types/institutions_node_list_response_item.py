

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .institutions_node_list_response_item_attributes import InstitutionsNodeListResponseItemAttributes
from .institutions_node_list_response_item_links import InstitutionsNodeListResponseItemLinks
from .institutions_node_list_response_item_relationships import InstitutionsNodeListResponseItemRelationships


class InstitutionsNodeListResponseItem(UniversalBaseModel):
    attributes: InstitutionsNodeListResponseItemAttributes = pydantic.Field()
    """
    The properties of the node entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the node entity.
    """

    links: typing.Optional[InstitutionsNodeListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the node entity.
    """

    relationships: typing.Optional[InstitutionsNodeListResponseItemRelationships] = pydantic.Field(default=None)
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
