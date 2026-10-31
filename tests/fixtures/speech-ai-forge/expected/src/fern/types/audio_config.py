

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .audio_format import AudioFormat


class AudioConfig(UniversalBaseModel):
    audio_encoding: typing_extensions.Annotated[
        typing.Optional[AudioFormat], FieldMetadata(alias="audioEncoding"), pydantic.Field(alias="audioEncoding")
    ] = None
    audio_bitrate: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="audioBitrate"), pydantic.Field(alias="audioBitrate")
    ] = None
    speaking_rate: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="speakingRate"), pydantic.Field(alias="speakingRate")
    ] = None
    pitch: typing.Optional[float] = None
    volume_gain_db: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="volumeGainDb"), pydantic.Field(alias="volumeGainDb")
    ] = None
    sample_rate_hertz: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sampleRateHertz"), pydantic.Field(alias="sampleRateHertz")
    ] = None
    batch_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="batchSize"), pydantic.Field(alias="batchSize")
    ] = None
    spliter_threshold: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="spliterThreshold"), pydantic.Field(alias="spliterThreshold")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
