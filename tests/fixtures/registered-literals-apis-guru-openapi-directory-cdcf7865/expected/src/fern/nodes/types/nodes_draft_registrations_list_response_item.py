

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_draft_registrations_list_response_item_attributes import NodesDraftRegistrationsListResponseItemAttributes
from .nodes_draft_registrations_list_response_item_links import NodesDraftRegistrationsListResponseItemLinks
from .nodes_draft_registrations_list_response_item_relationships import (
    NodesDraftRegistrationsListResponseItemRelationships,
)


class NodesDraftRegistrationsListResponseItem(UniversalBaseModel):
    attributes: NodesDraftRegistrationsListResponseItemAttributes = pydantic.Field()
    """
    The properties of the Draft Registration entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the draft registration entity.
    """

    links: typing.Optional[NodesDraftRegistrationsListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the draft registration entity.
    """

    relationships: typing.Optional[NodesDraftRegistrationsListResponseItemRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the draft registration entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the draft registration entity (`draft_registrations`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
