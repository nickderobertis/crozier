

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .product_status_breakdown_refresh_interval import ProductStatusBreakdownRefreshInterval


class ProductStatusBreakdown(UniversalBaseModel):
    """
    A detailed breakdown of the institution's performance for a request type. The values for `success`, `error_plaid`, and `error_institution` sum to 1. The time range used for calculating the breakdown may range from the most recent few minutes to the past six hours. In general, smaller institutions will show status that was calculated over a longer period of time. For Investment updates, which are refreshed less frequently, the period assessed may be 24 hours or more. For more details, see [Institution status details](https://plaid.com/docs/account/activity/#institution-status-details).
    """

    error_institution: float = pydantic.Field()
    """
    The percentage of logins that are failing due to an issue in the institution's system, expressed as a decimal.
    """

    error_plaid: float = pydantic.Field()
    """
    The percentage of logins that are failing due to an internal Plaid issue, expressed as a decimal.
    """

    refresh_interval: typing.Optional[ProductStatusBreakdownRefreshInterval] = pydantic.Field(default=None)
    """
    The `refresh_interval` may be `DELAYED` or `STOPPED` even when the success rate is high. This value is only returned for Transactions status breakdowns.
    """

    success: float = pydantic.Field()
    """
    The percentage of login attempts that are successful, expressed as a decimal.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
