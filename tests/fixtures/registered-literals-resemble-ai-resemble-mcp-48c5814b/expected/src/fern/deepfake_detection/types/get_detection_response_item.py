

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.detect_audio_metrics import DetectAudioMetrics
from ...types.detect_image_metrics import DetectImageMetrics
from ...types.detect_video_metrics import DetectVideoMetrics
from .get_detection_response_item_audio_source_tracing import GetDetectionResponseItemAudioSourceTracing
from .get_detection_response_item_intelligence import GetDetectionResponseItemIntelligence
from .get_detection_response_item_media_type import GetDetectionResponseItemMediaType
from .get_detection_response_item_status import GetDetectionResponseItemStatus


class GetDetectionResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    media_type: typing.Optional[GetDetectionResponseItemMediaType] = None
    status: typing.Optional[GetDetectionResponseItemStatus] = None
    metrics: typing.Optional[DetectAudioMetrics] = None
    image_metrics: typing.Optional[DetectImageMetrics] = None
    video_metrics: typing.Optional[DetectVideoMetrics] = None
    audio_source_tracing: typing.Optional[GetDetectionResponseItemAudioSourceTracing] = pydantic.Field(default=None)
    """
    Source tracing results (only returned if audio is labeled fake)
    """

    intelligence: typing.Optional[GetDetectionResponseItemIntelligence] = pydantic.Field(default=None)
    """
    Intelligence results when requested
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to the media file. Null when Zero Retention Modeon Modeon Modeon Modeon Modeon Modeon Mode is enabled.
    """

    audio_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Alias of url. Null when Zero Retention Mode is enabled.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    Original filename, or tokenized (redacted_<token>.<ext>) when Zero Retention Mode is enabled
    """

    duration: typing.Optional[float] = None
    zero_retention_mode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether Zero Retention Mode is enabled for this detect
    """

    media_redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True when Zero Retention Mode is active and media URLs are redacted
    """

    media_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True when the source file has been permanently deleted from storage
    """

    file_deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO 8601 timestamp of when the file was purged, or null if not yet deleted
    """

    pipeline: typing.Optional[str] = pydantic.Field(default=None)
    """
    Legacy field. May be present on older image/video detects. Ignored for new detections.
    """

    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
