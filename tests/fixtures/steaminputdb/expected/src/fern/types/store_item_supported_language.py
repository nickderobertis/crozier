

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreItemSupportedLanguage(UniversalBaseModel):
    eadditionallanguage: typing.Optional[int] = None
    elanguage: typing.Optional[int] = None
    full_audio: typing.Optional[bool] = None
    subtitles: typing.Optional[bool] = None
    supported: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
