

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_key_usage_response_usage_api_keys import ApiKeyUsageResponseUsageApiKeys
from .api_key_usage_response_usage_by_key_item import ApiKeyUsageResponseUsageByKeyItem
from .api_key_usage_response_usage_period import ApiKeyUsageResponseUsagePeriod
from .api_key_usage_response_usage_requests import ApiKeyUsageResponseUsageRequests


class ApiKeyUsageResponseUsage(UniversalBaseModel):
    period: ApiKeyUsageResponseUsagePeriod
    requests: ApiKeyUsageResponseUsageRequests
    api_keys: typing_extensions.Annotated[
        ApiKeyUsageResponseUsageApiKeys, FieldMetadata(alias="apiKeys"), pydantic.Field(alias="apiKeys")
    ]
    by_key: typing_extensions.Annotated[
        typing.List[ApiKeyUsageResponseUsageByKeyItem], FieldMetadata(alias="byKey"), pydantic.Field(alias="byKey")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
