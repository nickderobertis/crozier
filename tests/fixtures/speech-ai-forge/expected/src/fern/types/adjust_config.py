

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AdjustConfig(UniversalBaseModel):
    pitch: typing.Optional[float] = None
    speed_rate: typing.Optional[float] = None
    volume_gain_db: typing.Optional[float] = None
    normalize: typing.Optional[bool] = None
    headroom: typing.Optional[float] = None
    remove_silence: typing.Optional[bool] = None
    remove_silence_threshold: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
