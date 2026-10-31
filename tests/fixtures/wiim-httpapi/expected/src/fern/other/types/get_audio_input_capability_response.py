

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_audio_input_capability_response_audio_input_item import GetAudioInputCapabilityResponseAudioInputItem


class GetAudioInputCapabilityResponse(UniversalBaseModel):
    ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    Audio input capability version
    """

    audio_input: typing_extensions.Annotated[
        typing.Optional[typing.List[GetAudioInputCapabilityResponseAudioInputItem]],
        FieldMetadata(alias="audioInput"),
        pydantic.Field(alias="audioInput", description="List of supported audio input modes"),
    ] = None
    """
    List of supported audio input modes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
