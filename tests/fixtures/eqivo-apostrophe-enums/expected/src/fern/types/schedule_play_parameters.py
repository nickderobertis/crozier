

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_play_parameters_legs import SchedulePlayParametersLegs


class SchedulePlayParameters(UniversalBaseModel):
    call_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Unique identifier of the call to play media into"),
    ]
    """
    Unique identifier of the call to play media into
    """

    legs: typing_extensions.Annotated[
        typing.Optional[SchedulePlayParametersLegs],
        FieldMetadata(alias="Legs"),
        pydantic.Field(
            alias="Legs",
            description="Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.",
        ),
    ] = None
    """
    Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.
    """

    length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Length"),
        pydantic.Field(alias="Length", description="Maximum amount of time (in seconds) to playback the media"),
    ] = None
    """
    Maximum amount of time (in seconds) to playback the media
    """

    loop: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Loop"),
        pydantic.Field(alias="Loop", description="Loops the media file(s) indefinitely"),
    ] = None
    """
    Loops the media file(s) indefinitely
    """

    mix: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Mix"),
        pydantic.Field(alias="Mix", description="Whether the media should be mixed with the call's audio stream"),
    ] = None
    """
    Whether the media should be mixed with the call's audio stream
    """

    sounds: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Sounds"),
        pydantic.Field(alias="Sounds", description="Comma separated list of file paths/URIs to be played"),
    ]
    """
    Comma separated list of file paths/URIs to be played
    """

    time: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Time"),
        pydantic.Field(alias="Time", description="Time (in seconds) after which the media will be playedback"),
    ]
    """
    Time (in seconds) after which the media will be playedback
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
