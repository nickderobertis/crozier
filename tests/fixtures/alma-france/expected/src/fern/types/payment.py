

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .order import Order
from .payment_plan_item import PaymentPlanItem


class Payment(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique payment identifier
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment status
    """

    purchase_amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    Purchase amount in cents
    """

    customer_fee: typing.Optional[int] = pydantic.Field(default=None)
    """
    Customer fee in cents
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Creation timestamp
    """

    payment_plan: typing.Optional[typing.List[PaymentPlanItem]] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment page URL
    """

    return_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return URL after payment
    """

    orders: typing.Optional[typing.List[Order]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
