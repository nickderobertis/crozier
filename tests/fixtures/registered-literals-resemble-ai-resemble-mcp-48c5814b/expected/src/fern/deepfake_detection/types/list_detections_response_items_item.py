

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.detect_audio_metrics import DetectAudioMetrics
from ...types.detect_image_metrics import DetectImageMetrics
from ...types.detect_video_metrics import DetectVideoMetrics
from .list_detections_response_items_item_audio_source_tracing import ListDetectionsResponseItemsItemAudioSourceTracing
from .list_detections_response_items_item_media_type import ListDetectionsResponseItemsItemMediaType
from .list_detections_response_items_item_status import ListDetectionsResponseItemsItemStatus


class ListDetectionsResponseItemsItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    media_type: typing.Optional[ListDetectionsResponseItemsItemMediaType] = None
    status: typing.Optional[ListDetectionsResponseItemsItemStatus] = None
    metrics: typing.Optional[DetectAudioMetrics] = None
    image_metrics: typing.Optional[DetectImageMetrics] = None
    video_metrics: typing.Optional[DetectVideoMetrics] = None
    audio_source_tracing: typing.Optional[ListDetectionsResponseItemsItemAudioSourceTracing] = pydantic.Field(
        default=None
    )
    """
    Source tracing results (only returned if audio is labeled fake)
    """

    intelligence: typing.Optional[typing.Dict[str, typing.Any]] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to the media file. Null when Zero Retention Mode is enabled.
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
    Whether Zero Retention Mode was enabled for this detect
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

    visualize: typing.Optional[bool] = None
    audio_source_tracing_enabled: typing.Optional[bool] = None
    use_ood_detector: typing.Optional[bool] = None
    pipeline: typing.Optional[str] = pydantic.Field(default=None)
    """
    Legacy field. May be present on older image/video detects. Ignored on create for new detections.
    """

    extra_params: typing.Optional[typing.Dict[str, typing.Any]] = None
    error_message: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
