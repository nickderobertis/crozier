

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FlowAudioEssenceParametersCodecParameters(UniversalBaseModel):
    coded_frame_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The fixed number of samples per coded audio frame.
    """

    mp4oti: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="mp4_oti"),
        pydantic.Field(
            alias="mp4_oti",
            description="The MPEG-4 Object Type Identification. For more information on the use of this property in codec strings, see https://developer.mozilla.org/en-US/docs/Web/Media/Formats/codecs_parameter#mpeg-4_audio",
        ),
    ] = None
    """
    The MPEG-4 Object Type Identification. For more information on the use of this property in codec strings, see https://developer.mozilla.org/en-US/docs/Web/Media/Formats/codecs_parameter#mpeg-4_audio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
