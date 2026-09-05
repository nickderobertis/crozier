

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_param_developer_content import ChatCompletionMessageParamDeveloperContent


class ChatCompletionMessageParamDeveloper(UniversalBaseModel):
    content: typing.Optional[ChatCompletionMessageParamDeveloperContent] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
