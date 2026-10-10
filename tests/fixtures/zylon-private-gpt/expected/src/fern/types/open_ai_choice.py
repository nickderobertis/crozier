

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chunk import Chunk
from .open_ai_delta import OpenAiDelta
from .open_ai_message import OpenAiMessage


class OpenAiChoice(UniversalBaseModel):
    """
    Response from AI.

    Either the delta or the message will be present, but never both.
    Sources used will be returned in case context retrieval was enabled.
    """

    finish_reason: typing.Optional[str] = None
    delta: typing.Optional[OpenAiDelta] = None
    message: typing.Optional[OpenAiMessage] = None
    sources: typing.Optional[typing.List[Chunk]] = None
    index: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
