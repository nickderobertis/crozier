

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ElevenLabsVoice(UniversalBaseModel):
    id: str
    user_id: str
    voice_id: str
    stability: typing.Optional[float] = None
    similarity_boost: typing.Optional[float] = None
    api_key: typing.Optional[str] = None
    optimize_streaming_latency: typing.Optional[int] = None
    model_id: typing.Optional[str] = None
    experimental_input_streaming: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
