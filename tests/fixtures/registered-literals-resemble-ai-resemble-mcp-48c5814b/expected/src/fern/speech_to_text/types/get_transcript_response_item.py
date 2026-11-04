

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_transcript_response_item_status import GetTranscriptResponseItemStatus
from .get_transcript_response_item_words_item import GetTranscriptResponseItemWordsItem


class GetTranscriptResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    status: typing.Optional[GetTranscriptResponseItemStatus] = None
    text: typing.Optional[str] = None
    words: typing.Optional[typing.List[GetTranscriptResponseItemWordsItem]] = None
    duration_seconds: typing.Optional[float] = None
    file_url: typing.Optional[str] = None
    query: typing.Optional[str] = None
    answer: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
