

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_mapping_audio_track import ContainerMappingAudioTrack
from .container_mapping_isobmff_container import ContainerMappingIsobmffContainer
from .container_mapping_mp2ts_container import ContainerMappingMp2TsContainer
from .container_mapping_mxf_container import ContainerMappingMxfContainer


class ContainerMapping(UniversalBaseModel):
    """
    Defines the location of Flow essence data in a container track
    """

    track_index: typing.Optional[int] = pydantic.Field(default=None)
    """
    A zero-based and sequential track index in the container. This assumes a reliable ordering of tracks
    """

    format_track_index: typing.Optional[int] = pydantic.Field(default=None)
    """
    A zero-based and sequential track index in the container for a particular Flow format. A container with a video and 2 audio tracks would have a format_track_index 0 for the video Flow and format_track_index 0 and 1 for the audio Flows. This assumes a reliable ordering of tracks for each Flow format
    """

    audio_track: typing.Optional[ContainerMappingAudioTrack] = pydantic.Field(default=None)
    """
    Mapping for channels in audio tracks to the Flow channels
    """

    mp2ts_container: typing.Optional[ContainerMappingMp2TsContainer] = pydantic.Field(default=None)
    """
    Mapping to MPEG-2 Transport Stream containers, ISO/IEC 13818-1 or ITU-T Recommendation H.222.0
    """

    mxf_container: typing.Optional[ContainerMappingMxfContainer] = pydantic.Field(default=None)
    """
    Mapping to Material Exchange Format containers, SMPTE ST 377-1
    """

    isobmff_container: typing.Optional[ContainerMappingIsobmffContainer] = pydantic.Field(default=None)
    """
    Mapping to ISO Base Media File Format (e.g. MP4 and MOV) containers, ISO/IEC 14496-12
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
