

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .non_empty_id import NonEmptyId


class AuditFields(UniversalBaseModel):
    audited_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="auditedAt"), pydantic.Field(alias="auditedAt")
    ]
    audited_by: typing_extensions.Annotated[
        NonEmptyId, FieldMetadata(alias="auditedBy"), pydantic.Field(alias="auditedBy")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
