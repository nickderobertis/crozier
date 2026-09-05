

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response import AccountResponse
from .guild_subscription_integration_response_type import GuildSubscriptionIntegrationResponseType
from .snowflake_type import SnowflakeType


class GuildSubscriptionIntegrationResponse(UniversalBaseModel):
    type: GuildSubscriptionIntegrationResponseType
    name: typing.Optional[str] = None
    account: typing.Optional[AccountResponse] = None
    enabled: typing.Optional[bool] = None
    id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
