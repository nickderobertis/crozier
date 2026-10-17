

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rime_voice_model_id import RimeVoiceModelId


class RimeVoice(UniversalBaseModel):
    id: str
    user_id: str
    speaker: str
    speed_alpha: typing.Optional[float] = None
    model_id: typing.Optional[RimeVoiceModelId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
