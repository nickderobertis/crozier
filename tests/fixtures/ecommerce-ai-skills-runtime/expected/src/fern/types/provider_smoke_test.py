

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_smoke_provider import ProviderSmokeProvider
from .provider_smoke_test_status import ProviderSmokeTestStatus


class ProviderSmokeTest(UniversalBaseModel):
    id: str
    tenant_id: str
    provider: ProviderSmokeProvider
    connector_account_id: typing.Optional[str] = None
    created_by: str
    status: ProviderSmokeTestStatus
    provider_request_id: typing.Optional[str] = None
    provider_status: typing.Optional[str] = None
    http_status: typing.Optional[int] = None
    retry_after_seconds: typing.Optional[int] = None
    latency_ms: typing.Optional[int] = None
    error_code: typing.Optional[str] = None
    created_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
