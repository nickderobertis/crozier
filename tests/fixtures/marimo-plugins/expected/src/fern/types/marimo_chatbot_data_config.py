

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MarimoChatbotDataConfig(UniversalBaseModel):
    max_tokens: typing.Optional[float] = None
    temperature: typing.Optional[float] = None
    top_p: typing.Optional[float] = None
    top_k: typing.Optional[float] = None
    frequency_penalty: typing.Optional[float] = None
    presence_penalty: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
