

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_attachment_kind import ActionAttachmentKind


class ActionAttachment(UniversalBaseModel):
    id: str
    name: str
    type: str
    kind: ActionAttachmentKind
    url: str
    size: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
