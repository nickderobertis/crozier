

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parse_billing_service_tier import ParseBillingServiceTier


class ParseBilling(UniversalBaseModel):
    """
    Billing summary for one parse request.
    """

    service_tier: typing.Optional[ParseBillingServiceTier] = pydantic.Field(default=None)
    """
    The service tier the request ran in: `standard` or `priority`. A sync request reports `priority` (same lane, same price).
    """

    total_credits: typing.Optional[float] = pydantic.Field(default=None)
    """
    Credits charged for this request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
