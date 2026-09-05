

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response import AccountResponse
from .discord_integration_response_scopes_item import DiscordIntegrationResponseScopesItem
from .discord_integration_response_type import DiscordIntegrationResponseType
from .integration_application_response import IntegrationApplicationResponse
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class DiscordIntegrationResponse(UniversalBaseModel):
    type: DiscordIntegrationResponseType
    name: typing.Optional[str] = None
    account: typing.Optional[AccountResponse] = None
    enabled: typing.Optional[bool] = None
    id: SnowflakeType
    application: IntegrationApplicationResponse
    scopes: typing.List[DiscordIntegrationResponseScopesItem]
    user: typing.Optional[UserResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
