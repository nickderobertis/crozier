

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_param import ChatCompletionMessageParam
from .prompt_block_data_nullish_messages_type import PromptBlockDataNullishMessagesType


class PromptBlockDataNullishMessages(UniversalBaseModel):
    type: PromptBlockDataNullishMessagesType
    messages: typing.List[ChatCompletionMessageParam]
    tools: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
