

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TtsConfig(UniversalBaseModel):
    mid: typing.Optional[str] = None
    style: typing.Optional[str] = None
    temperature: typing.Optional[float] = None
    top_p: typing.Optional[float] = None
    top_k: typing.Optional[int] = None
    prompt: typing.Optional[str] = None
    prompt1: typing.Optional[str] = None
    prompt2: typing.Optional[str] = None
    prefix: typing.Optional[str] = None
    emotion: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
