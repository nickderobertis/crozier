

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_watermark_detection_result_response_item_media_type import GetWatermarkDetectionResultResponseItemMediaType
from .get_watermark_detection_result_response_item_metrics import GetWatermarkDetectionResultResponseItemMetrics


class GetWatermarkDetectionResultResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    media_type: typing.Optional[GetWatermarkDetectionResultResponseItemMediaType] = None
    source_media_url: typing.Optional[str] = None
    metrics: typing.Optional[GetWatermarkDetectionResultResponseItemMetrics] = pydantic.Field(default=None)
    """
    Detection results including has_watermark. Audio also includes confidence.
    """

    watermarked_media: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
