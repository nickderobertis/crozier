

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_draft_registrations_subjects_response_attributes import NodesDraftRegistrationsSubjectsResponseAttributes
from .nodes_draft_registrations_subjects_response_embeds import NodesDraftRegistrationsSubjectsResponseEmbeds
from .nodes_draft_registrations_subjects_response_links import NodesDraftRegistrationsSubjectsResponseLinks
from .nodes_draft_registrations_subjects_response_relationships import (
    NodesDraftRegistrationsSubjectsResponseRelationships,
)


class NodesDraftRegistrationsSubjectsResponse(UniversalBaseModel):
    attributes: typing.Optional[NodesDraftRegistrationsSubjectsResponseAttributes] = pydantic.Field(default=None)
    """
    The attributes of the Subject.
    """

    embeds: typing.Optional[NodesDraftRegistrationsSubjectsResponseEmbeds] = pydantic.Field(default=None)
    """
    The parent is always embedded in the Subject response.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Subject.
    """

    links: typing.Optional[NodesDraftRegistrationsSubjectsResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the Subject entity.
    """

    relationships: typing.Optional[NodesDraftRegistrationsSubjectsResponseRelationships] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the file entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the Subject (`subject`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
