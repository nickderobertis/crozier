

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sound_touch_parameters_audio_direction import SoundTouchParametersAudioDirection


class SoundTouchParameters(UniversalBaseModel):
    audio_direction: typing_extensions.Annotated[
        typing.Optional[SoundTouchParametersAudioDirection],
        FieldMetadata(alias="AudioDirection"),
        pydantic.Field(alias="AudioDirection", description="Media stream to be altered, incoming or outgoing"),
    ] = None
    """
    Media stream to be altered, incoming or outgoing
    """

    call_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Unique identifier of the call to send DTMF to"),
    ]
    """
    Unique identifier of the call to send DTMF to
    """

    pitch: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Pitch"),
        pydantic.Field(alias="Pitch", description="Adjust the pitch"),
    ] = None
    """
    Adjust the pitch
    """

    pitch_octaves: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="PitchOctaves"),
        pydantic.Field(alias="PitchOctaves", description="Adjust the pitch in octaves"),
    ] = None
    """
    Adjust the pitch in octaves
    """

    pitch_semi_tones: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="PitchSemiTones"),
        pydantic.Field(alias="PitchSemiTones", description="Adjust the pitch in semitones"),
    ] = None
    """
    Adjust the pitch in semitones
    """

    rate: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="Rate"), pydantic.Field(alias="Rate", description="Adjust the rate")
    ] = None
    """
    Adjust the rate
    """

    tempo: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Tempo"),
        pydantic.Field(alias="Tempo", description="Adjust the tempo"),
    ] = None
    """
    Adjust the tempo
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
