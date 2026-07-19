

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .templates_create_agents_from_template_no_project_request_initial_message_sequence_item_role import (
    TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole,
)


class TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItem(UniversalBaseModel):
    role: TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole
    content: str
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    batch_item_id: typing.Optional[str] = None
    group_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
