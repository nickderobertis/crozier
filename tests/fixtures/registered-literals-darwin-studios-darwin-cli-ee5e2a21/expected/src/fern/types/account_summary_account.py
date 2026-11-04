

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_summary_account_time_zone import AccountSummaryAccountTimeZone


class AccountSummaryAccount(UniversalBaseModel):
    name: typing.Optional[str] = None
    avatar_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="avatarUrl"), pydantic.Field(alias="avatarUrl")
    ] = None
    time_zone: typing_extensions.Annotated[
        AccountSummaryAccountTimeZone, FieldMetadata(alias="timeZone"), pydantic.Field(alias="timeZone")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
