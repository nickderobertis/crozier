

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_assistant_message_content import UpdateAssistantMessageContent


class UpdateAssistantMessage(UniversalBaseModel):
    content: UpdateAssistantMessageContent = pydantic.Field()
    """
    The message content sent by the assistant (can be a string or an array of content parts)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
