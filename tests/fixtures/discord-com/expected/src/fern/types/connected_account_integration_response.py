

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response import AccountResponse
from .connected_account_guild_response import ConnectedAccountGuildResponse
from .integration_types import IntegrationTypes


class ConnectedAccountIntegrationResponse(UniversalBaseModel):
    id: str
    type: IntegrationTypes
    account: AccountResponse
    guild: ConnectedAccountGuildResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
