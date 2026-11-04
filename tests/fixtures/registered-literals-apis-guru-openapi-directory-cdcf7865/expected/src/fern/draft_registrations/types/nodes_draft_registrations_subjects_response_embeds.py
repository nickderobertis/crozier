

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_draft_registrations_subjects_response_embeds_parent import (
    NodesDraftRegistrationsSubjectsResponseEmbedsParent,
)


class NodesDraftRegistrationsSubjectsResponseEmbeds(UniversalBaseModel):
    """
    The parent is always embedded in the Subject response.
    """

    parent: typing.Optional[NodesDraftRegistrationsSubjectsResponseEmbedsParent] = pydantic.Field(default=None)
    """
    The parent of the Subject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
