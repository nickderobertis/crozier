

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response import AccountResponse
from .partial_external_connection_integration_response_type import PartialExternalConnectionIntegrationResponseType
from .snowflake_type import SnowflakeType


class PartialExternalConnectionIntegrationResponse(UniversalBaseModel):
    id: SnowflakeType
    type: PartialExternalConnectionIntegrationResponseType
    name: typing.Optional[str] = None
    account: typing.Optional[AccountResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
