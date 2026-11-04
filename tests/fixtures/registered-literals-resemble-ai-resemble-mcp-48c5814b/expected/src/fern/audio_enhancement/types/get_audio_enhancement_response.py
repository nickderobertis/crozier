

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_audio_enhancement_response_status import GetAudioEnhancementResponseStatus


class GetAudioEnhancementResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    status: typing.Optional[GetAudioEnhancementResponseStatus] = None
    enhanced_audio_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Download URL. Only present when status is completed. This is a temporary signed URL.
    """

    error_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable error. Only present when status is failed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
