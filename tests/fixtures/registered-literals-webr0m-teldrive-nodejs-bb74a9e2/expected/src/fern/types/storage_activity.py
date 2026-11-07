

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StorageActivity(UniversalBaseModel):
    id: int
    type: str
    resource_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="resourceType"), pydantic.Field(alias="resourceType")
    ]
    resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")
    ] = None
    label: str
    occurred_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="occurredAt"), pydantic.Field(alias="occurredAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
