

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_filter import ContextFilter
from .open_ai_message import OpenAiMessage


class ChatBody(UniversalBaseModel):
    messages: typing.List[OpenAiMessage]
    use_context: typing.Optional[bool] = None
    context_filter: typing.Optional[ContextFilter] = None
    include_sources: typing.Optional[bool] = None
    stream: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
