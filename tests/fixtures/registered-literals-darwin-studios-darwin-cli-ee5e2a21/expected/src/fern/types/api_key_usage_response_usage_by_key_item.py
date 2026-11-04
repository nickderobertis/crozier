

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_key_usage_response_usage_by_key_item_status import ApiKeyUsageResponseUsageByKeyItemStatus


class ApiKeyUsageResponseUsageByKeyItem(UniversalBaseModel):
    id: str
    name: str
    prefix: str
    status: ApiKeyUsageResponseUsageByKeyItemStatus
    request_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="requestCount"), pydantic.Field(alias="requestCount")
    ]
    last_used_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUsedAt"), pydantic.Field(alias="lastUsedAt")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
