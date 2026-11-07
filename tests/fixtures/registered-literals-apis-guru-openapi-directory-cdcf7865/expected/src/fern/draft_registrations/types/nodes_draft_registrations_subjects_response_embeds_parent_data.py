

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_draft_registrations_subjects_response_embeds_parent_data_attributes import (
    NodesDraftRegistrationsSubjectsResponseEmbedsParentDataAttributes,
)
from .nodes_draft_registrations_subjects_response_embeds_parent_data_relationships import (
    NodesDraftRegistrationsSubjectsResponseEmbedsParentDataRelationships,
)


class NodesDraftRegistrationsSubjectsResponseEmbedsParentData(UniversalBaseModel):
    attributes: typing.Optional[NodesDraftRegistrationsSubjectsResponseEmbedsParentDataAttributes] = pydantic.Field(
        default=None
    )
    """
    The attributes of the Subject.
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A JSON object containing the embedded information.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Subject.
    """

    relationships: typing.Optional[NodesDraftRegistrationsSubjectsResponseEmbedsParentDataRelationships] = (
        pydantic.Field(default=None)
    )
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
