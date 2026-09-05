

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response import AccountResponse
from .partial_discord_integration_response_type import PartialDiscordIntegrationResponseType
from .snowflake_type import SnowflakeType


class PartialDiscordIntegrationResponse(UniversalBaseModel):
    id: SnowflakeType
    type: PartialDiscordIntegrationResponseType
    name: typing.Optional[str] = None
    account: typing.Optional[AccountResponse] = None
    application_id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
