

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_system_message_param_content import ChatCompletionSystemMessageParamContent


class ChatCompletionSystemMessageParam(UniversalBaseModel):
    """
    Developer-provided instructions that the model should follow, regardless of
    messages sent by the user. With o1 models and newer, use `developer` messages
    for this purpose instead.
    """

    content: ChatCompletionSystemMessageParamContent
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
