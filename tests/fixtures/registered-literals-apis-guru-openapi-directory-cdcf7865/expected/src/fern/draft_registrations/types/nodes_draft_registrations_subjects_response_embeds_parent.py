

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_draft_registrations_subjects_response_embeds_parent_data import (
    NodesDraftRegistrationsSubjectsResponseEmbedsParentData,
)


class NodesDraftRegistrationsSubjectsResponseEmbedsParent(UniversalBaseModel):
    """
    The parent of the Subject.
    """

    data: typing.Optional[NodesDraftRegistrationsSubjectsResponseEmbedsParentData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
