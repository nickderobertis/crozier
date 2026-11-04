

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_message import ChatMessage
from .chat_source import ChatSource


class PostChatCompletionResponse(UniversalBaseModel):
    turns: typing.List[ChatMessage] = pydantic.Field()
    """
    The conversation turns in the chat completion
    """

    citations: typing.List[str] = pydantic.Field()
    """
    List of citation strings
    """

    sources: typing.Optional[typing.List[ChatSource]] = pydantic.Field(default=None)
    """
    Pages the answer was grounded in, one entry per cited page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
