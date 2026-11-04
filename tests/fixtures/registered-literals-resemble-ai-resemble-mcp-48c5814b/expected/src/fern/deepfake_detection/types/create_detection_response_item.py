

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_detection_response_item_intelligence import CreateDetectionResponseItemIntelligence


class CreateDetectionResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    status: typing.Optional[str] = None
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
    Original filename, or tokenized (redacted_<token>.<ext>) when Zero Retention Modeon Modeon Mode is enabled
    """

    intelligence: typing.Optional[CreateDetectionResponseItemIntelligence] = pydantic.Field(default=None)
    """
    Intelligence results when requested
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
