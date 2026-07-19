

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_video_essence_parameters_aspect_ratio import FlowVideoEssenceParametersAspectRatio
from .flow_video_essence_parameters_avc_parameters import FlowVideoEssenceParametersAvcParameters
from .flow_video_essence_parameters_colorspace import FlowVideoEssenceParametersColorspace
from .flow_video_essence_parameters_component_type import FlowVideoEssenceParametersComponentType
from .flow_video_essence_parameters_frame_rate import FlowVideoEssenceParametersFrameRate
from .flow_video_essence_parameters_interlace_mode import FlowVideoEssenceParametersInterlaceMode
from .flow_video_essence_parameters_pixel_aspect_ratio import FlowVideoEssenceParametersPixelAspectRatio
from .flow_video_essence_parameters_transfer_characteristic import FlowVideoEssenceParametersTransferCharacteristic
from .flow_video_essence_parameters_unc_parameters import FlowVideoEssenceParametersUncParameters


class FlowVideoEssenceParameters(UniversalBaseModel):
    """
    Describes the parameters of the essence inside this video Flow
    """

    frame_width: int = pydantic.Field()
    """
    The width of the picture in pixels.
    """

    frame_height: int = pydantic.Field()
    """
    The height of the picture in pixels.
    """

    bit_depth: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of significant bits used to represent the video component sample. If codec is `video/raw`, bit_depth must be set.
    """

    interlace_mode: typing.Optional[FlowVideoEssenceParametersInterlaceMode] = pydantic.Field(default=None)
    """
    Interlaced video mode for frames in this Flow
    """

    colorspace: typing.Optional[FlowVideoEssenceParametersColorspace] = pydantic.Field(default=None)
    """
    Colorspace used for the video
    """

    transfer_characteristic: typing.Optional[FlowVideoEssenceParametersTransferCharacteristic] = pydantic.Field(
        default=None
    )
    """
    Transfer characteristic
    """

    aspect_ratio: typing.Optional[FlowVideoEssenceParametersAspectRatio] = pydantic.Field(default=None)
    """
    The display aspect ratio. i.e. display_width / display_height
    """

    pixel_aspect_ratio: typing.Optional[FlowVideoEssenceParametersPixelAspectRatio] = pydantic.Field(default=None)
    """
    The pixel aspect ratio. This is usually 1:1 (i.e. square pixels) for modern video. Some, usually older, video formats use non-square pixels e.g. some Standard Definition video. This is where that may be indicated.
    """

    component_type: typing.Optional[FlowVideoEssenceParametersComponentType] = pydantic.Field(default=None)
    """
    Picture component representation.
    """

    horiz_chroma_subs: typing.Optional[int] = pydantic.Field(default=None)
    """
    Horizontal chroma component sub-sampling. When unc_type is set to a YUV type, horiz_chroma_subs must be set.
    """

    vert_chroma_subs: typing.Optional[int] = pydantic.Field(default=None)
    """
    Vertical chroma component sub-sampling. When unc_type is set to a YUV type, vert_chroma_subs must be set.
    """

    unc_parameters: typing.Optional[FlowVideoEssenceParametersUncParameters] = None
    avc_parameters: typing.Optional[FlowVideoEssenceParametersAvcParameters] = None
    frame_rate: typing.Optional[FlowVideoEssenceParametersFrameRate] = pydantic.Field(default=None)
    """
    The fixed number of frames per second. MUST be set if `vfr` is `false` or omitted. MUST NOT be set if `vfr` is `true`.
    """

    vfr: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the frame rate of the Flow is variable and `frame_rate` MUST NOT be set. If `false` or omitted, the frame rate of the Flow is fixed and `frame_rate` MUST be set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
