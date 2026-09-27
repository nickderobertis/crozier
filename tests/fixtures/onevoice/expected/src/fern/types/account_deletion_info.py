

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccountDeletionInfo(UniversalBaseModel):
    requested_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="requestedAt"), pydantic.Field(alias="requestedAt")
    ]
    scheduled_deletion_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="scheduledDeletionAt"), pydantic.Field(alias="scheduledDeletionAt")
    ]
    can_restore_until: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="canRestoreUntil"), pydantic.Field(alias="canRestoreUntil")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
