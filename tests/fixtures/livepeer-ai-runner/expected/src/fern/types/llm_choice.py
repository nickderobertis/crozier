

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .llm_message import LlmMessage


class LlmChoice(UniversalBaseModel):
    index: int
    finish_reason: typing.Optional[str] = None
    delta: typing.Optional[LlmMessage] = None
    message: typing.Optional[LlmMessage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
