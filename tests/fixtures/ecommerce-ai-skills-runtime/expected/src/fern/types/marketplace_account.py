

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_provider import ConnectorProvider
from .connector_provider_details import ConnectorProviderDetails
from .marketplace_account_credential_refs_value import MarketplaceAccountCredentialRefsValue
from .marketplace_account_health_error_code import MarketplaceAccountHealthErrorCode
from .marketplace_account_health_status import MarketplaceAccountHealthStatus


class MarketplaceAccount(UniversalBaseModel):
    id: str
    tenant_id: str
    provider: ConnectorProvider
    external_account_id: str
    provider_details: ConnectorProviderDetails
    credential_refs: typing.Dict[str, MarketplaceAccountCredentialRefsValue] = pydantic.Field()
    """
    Credential reference presence only; values are always present and never contain names or secrets.
    """

    health_status: MarketplaceAccountHealthStatus
    health_checked_at: typing.Optional[dt.datetime] = None
    health_error_code: typing.Optional[MarketplaceAccountHealthErrorCode] = None
    health_error_message: typing.Optional[str] = None
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
