

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response import AccountResponse
from .external_connection_integration_response_type import ExternalConnectionIntegrationResponseType
from .integration_expire_behavior_types import IntegrationExpireBehaviorTypes
from .integration_expire_grace_period_types import IntegrationExpireGracePeriodTypes
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class ExternalConnectionIntegrationResponse(UniversalBaseModel):
    type: ExternalConnectionIntegrationResponseType
    name: typing.Optional[str] = None
    account: typing.Optional[AccountResponse] = None
    enabled: typing.Optional[bool] = None
    id: str
    user: UserResponse
    revoked: typing.Optional[bool] = None
    expire_behavior: typing.Optional[IntegrationExpireBehaviorTypes] = None
    expire_grace_period: typing.Optional[IntegrationExpireGracePeriodTypes] = None
    subscriber_count: typing.Optional[int] = None
    synced_at: typing.Optional[dt.datetime] = None
    role_id: typing.Optional[SnowflakeType] = None
    syncing: typing.Optional[bool] = None
    enable_emoticons: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
