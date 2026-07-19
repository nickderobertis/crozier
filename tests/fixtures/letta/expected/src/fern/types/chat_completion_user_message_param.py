

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_user_message_param_content import ChatCompletionUserMessageParamContent


class ChatCompletionUserMessageParam(UniversalBaseModel):
    """
    Messages sent by an end user, containing prompts or additional context
    information.
    """

    content: ChatCompletionUserMessageParamContent
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
