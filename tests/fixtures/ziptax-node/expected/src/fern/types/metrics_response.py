

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetricsResponse(UniversalBaseModel):
    core_request_count: int = pydantic.Field()
    """
    Number of core (tax lookup) requests the account has consumed in the current billing period.
    """

    core_request_limit: int = pydantic.Field()
    """
    Maximum core requests allowed for the account in the current period, from the account's entitlement.
    """

    core_usage_percent: float = pydantic.Field()
    """
    Core request usage as a percentage of the limit (0–100).
    """

    geo_enabled: bool = pydantic.Field()
    """
    Whether the account has the geocoding (geo_enabled) entitlement that allows address and coordinate lookups.
    """

    geo_request_count: int = pydantic.Field()
    """
    Number of geocoding requests the account has consumed in the current period.
    """

    geo_request_limit: int = pydantic.Field()
    """
    Maximum geocoding requests allowed for the account in the current period.
    """

    geo_usage_percent: float = pydantic.Field()
    """
    Geocoding request usage as a percentage of the limit (0–100).
    """

    is_active: bool = pydantic.Field()
    """
    Whether the account is currently active and able to make requests.
    """

    merchant_request_count: int = pydantic.Field()
    """
    Number of merchant requests the account has consumed in the current period.
    """

    merchant_request_limit: int = pydantic.Field()
    """
    Maximum merchant requests allowed for the account in the current period.
    """

    merchant_usage_percent: float = pydantic.Field()
    """
    Merchant request usage as a percentage of the limit (0–100).
    """

    message: str = pydantic.Field()
    """
    Informational message about the account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
