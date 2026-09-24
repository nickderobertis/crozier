

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .quote_config import QuoteConfig
from .quote_deposit import QuoteDeposit
from .quote_links_item import QuoteLinksItem
from .quote_sections_item import QuoteSectionsItem


class Quote(UniversalBaseModel):
    id: float
    version_number: typing_extensions.Annotated[
        float, FieldMetadata(alias="versionNumber"), pydantic.Field(alias="versionNumber")
    ]
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    guid: typing.Optional[str] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    footer_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="footerText"), pydantic.Field(alias="footerText")
    ] = None
    quote_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="quoteDate"), pydantic.Field(alias="quoteDate")
    ] = None
    is_sent: typing_extensions.Annotated[bool, FieldMetadata(alias="isSent"), pydantic.Field(alias="isSent")]
    is_accepted: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isAccepted"), pydantic.Field(alias="isAccepted")
    ]
    is_superseded: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isSuperseded"), pydantic.Field(alias="isSuperseded")
    ]
    is_locked: typing_extensions.Annotated[bool, FieldMetadata(alias="isLocked"), pydantic.Field(alias="isLocked")]
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
    declined_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="declinedAt"), pydantic.Field(alias="declinedAt")
    ] = None
    voided_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="voidedAt"), pydantic.Field(alias="voidedAt")
    ] = None
    due_days: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dueDays"), pydantic.Field(alias="dueDays")
    ] = None
    accepted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="acceptedBy"), pydantic.Field(alias="acceptedBy")
    ] = None
    job_no: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="jobNo"), pydantic.Field(alias="jobNo")
    ] = None
    quote_config: typing_extensions.Annotated[
        typing.Optional[QuoteConfig], FieldMetadata(alias="quoteConfig"), pydantic.Field(alias="quoteConfig")
    ] = None
    sections: typing.Optional[typing.List[QuoteSectionsItem]] = None
    deposit: typing.Optional[QuoteDeposit] = None
    links: typing.Optional[typing.List[QuoteLinksItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Quote)
