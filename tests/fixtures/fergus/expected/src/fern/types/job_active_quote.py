

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JobActiveQuote(UniversalBaseModel):
    id: float
    version_number: typing_extensions.Annotated[
        float, FieldMetadata(alias="versionNumber"), pydantic.Field(alias="versionNumber")
    ]
    guid: typing.Optional[str] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    quote_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="quoteDate"), pydantic.Field(alias="quoteDate")
    ] = None
    is_sent: typing_extensions.Annotated[bool, FieldMetadata(alias="isSent"), pydantic.Field(alias="isSent")]
    is_accepted: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isAccepted"), pydantic.Field(alias="isAccepted")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    published_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="publishedAt"), pydantic.Field(alias="publishedAt")
    ] = None
    due_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dueDate"), pydantic.Field(alias="dueDate")
    ] = None
    due_days: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dueDays"), pydantic.Field(alias="dueDays")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
