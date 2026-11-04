

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RecordMessageRecord(UniversalBaseModel):
    """
    One record for one stream.
    """

    stream: str = pydantic.Field()
    """
    Stream (table) name this record belongs to.
    """

    data: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The record payload as a key-value map.
    """

    record_deleted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="recordDeleted"), pydantic.Field(alias="recordDeleted")
    ] = None
    emitted_at: dt.datetime = pydantic.Field()
    """
    ISO 8601 timestamp when the record was emitted by the source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
