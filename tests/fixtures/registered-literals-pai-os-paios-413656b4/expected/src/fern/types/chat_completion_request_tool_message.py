

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionRequestToolMessage(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    The contents of the tool message.
    """

    tool_call_id: str = pydantic.Field()
    """
    Tool call that this message is responding to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
