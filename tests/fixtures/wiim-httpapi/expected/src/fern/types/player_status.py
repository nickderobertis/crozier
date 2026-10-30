

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .player_status_status import PlayerStatusStatus


class PlayerStatus(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    0: Main or standalone device 
    1: Device is a Multiroom Guest
    """

    ch: typing.Optional[str] = pydantic.Field(default=None)
    """
    Active channel(s) 0: Stereo 1: Left 2: Right
    """

    mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    0: None 
    1: AirPlay or AirPlay 2 
    2: DLNA streaming 
    10: Playing network content, e.g. vTuner, Home Media Share, Amazon Music, Deezer, etc 
    11: playing UDISK (Local USB disk on device) 16: TF card playlist 20: playback start by HTTPAPI 
    31: Spotify Connect 
    32: TIDAL Connect 
    40: AUX-In/Line-In input mode 
    41: Bluetooth input mode 
    42: External storage 
    43: Optical-In input mode 
    47: Line-In #2 input mode 
    50: Mirror 
    51: USBDAC input mode 
    60: Voice mail
    99: The Device is a Guest in a Multiroom Zone
    """

    loop: typing.Optional[str] = pydantic.Field(default=None)
    """
    Is a Combination of SHUFFLE and REPEAT modes 0: SHUFFLE:
    disabled REPEAT: enabled - loop 1: SHUFFLE: disabled
    REPEAT: enabled - loop once 2: SHUFFLE: enabled REPEAT:
    enabled - loop 3: SHUFFLE: enabled REPEAT: disabled 4:
    SHUFFLE: disabled REPEAT: disabled 5: SHUFFLE: enabled
    REPEAT: enabled - loop once
    """

    eq: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preset number of the Equalizer
    """

    vendor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the stream source
    """

    status: typing.Optional[PlayerStatusStatus] = pydantic.Field(default=None)
    """
    Playback status stop: no audio selected play: playing
    audio load/loading: loading/buffering audio pause: audio
    paused
    """

    curpos: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current position, in ms
    """

    offset_pts: typing.Optional[str] = pydantic.Field(default=None)
    """
    Offset position, in ms
    """

    totlen: typing.Optional[str] = pydantic.Field(default=None)
    """
    Track duration in ms. Zero when playing a live stream.
    """

    title: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Title"),
        pydantic.Field(alias="Title", description="hexed string of the track title"),
    ] = None
    """
    hexed string of the track title
    """

    artist: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Artist"),
        pydantic.Field(alias="Artist", description="hexed string of the artist"),
    ] = None
    """
    hexed string of the artist
    """

    album: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Album"),
        pydantic.Field(alias="Album", description="hexed string of the album"),
    ] = None
    """
    hexed string of the album
    """

    alarmflag: typing.Optional[str] = None
    plicount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The total number of tracks in the playlist
    """

    plicurr: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current track index
    """

    vol: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current volume Value range is from 0 - 100. So can be
    considered a linear percentage (0% to 100%) of the volume.
    """

    mute: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current mute state 0: Not muted 1: Muted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
