

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .detect_watermark_response_item_media_type import DetectWatermarkResponseItemMediaType


class DetectWatermarkResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    media_type: typing.Optional[DetectWatermarkResponseItemMediaType] = None
    source_media_url: typing.Optional[str] = None
    metrics: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Detection results. Null while processing.
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
