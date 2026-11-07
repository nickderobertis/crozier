

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .apply_watermark_response_item_media_type import ApplyWatermarkResponseItemMediaType


class ApplyWatermarkResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    media_type: typing.Optional[ApplyWatermarkResponseItemMediaType] = pydantic.Field(default=None)
    """
    Detected media type of the source file.
    """

    source_media_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The original source URL provided in the request.
    """

    watermarked_media: typing.Optional[str] = pydantic.Field(default=None)
    """
    Signed URL to the watermarked file. Populated when processing is complete.
    """

    metrics: typing.Optional[typing.Dict[str, typing.Any]] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
