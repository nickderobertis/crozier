

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .product_status_breakdown import ProductStatusBreakdown
from .product_status_status import ProductStatusStatus


class ProductStatus(UniversalBaseModel):
    """
    A representation of the status health of a request type. Auth requests, Balance requests, Identity requests, Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item logins each have their own status object.
    """

    breakdown: ProductStatusBreakdown
    last_status_change: dt.datetime = pydantic.Field()
    """
    [ISO 8601](https://wikipedia.org/wiki/ISO_8601) formatted timestamp of the last status change for the institution.
    """

    status: ProductStatusStatus = pydantic.Field()
    """
    This field is deprecated in favor of the `breakdown` object, which provides more granular institution health data.
    
    `HEALTHY`: the majority of requests are successful
    `DEGRADED`: only some requests are successful
    `DOWN`: all requests are failing
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
