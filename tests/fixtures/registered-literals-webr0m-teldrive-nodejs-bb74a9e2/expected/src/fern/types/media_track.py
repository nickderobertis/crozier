

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .media_track_kind import MediaTrackKind


class MediaTrack(UniversalBaseModel):
    width: typing.Optional[float] = None
    height: typing.Optional[float] = None
    channels: typing.Optional[float] = None
    sample_rate: typing.Optional[float] = None
    bit_rate: typing.Optional[float] = None
    duration: typing.Optional[float] = None
    bits_per_raw_sample: typing.Optional[float] = None
    profile: typing.Optional[str] = None
    pix_fmt: typing.Optional[str] = None
    avg_frame_rate: typing.Optional[str] = None
    channel_layout: typing.Optional[str] = None
    color_space: typing.Optional[str] = None
    color_transfer: typing.Optional[str] = None
    color_primaries: typing.Optional[str] = None
    field_order: typing.Optional[str] = None
    index: int
    kind: MediaTrackKind
    codec: str
    language: str
    title: str
    default: bool
    bitmap: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
