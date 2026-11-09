

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_request_user_message_content import ChatCompletionRequestUserMessageContent


class ChatCompletionRequestUserMessage(UniversalBaseModel):
    content: ChatCompletionRequestUserMessageContent = pydantic.Field()
    """
    The contents of the user message.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional name for the participant. Provides the model information to differentiate between participants of the same role.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
