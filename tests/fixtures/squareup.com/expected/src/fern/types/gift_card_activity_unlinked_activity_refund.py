

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class GiftCardActivityUnlinkedActivityRefund(UniversalBaseModel):
    """
    Present only when `GiftCardActivityType` is UNLINKED_ACTIVITY_REFUND.
    """

    amount_money: Money
    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    When using the Square Payments API, the ID of the payment that was refunded to this gift
    card.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A client-specified ID to associate an entity, in another system, with this gift card
    activity. This can be used to track the order or payment related information when the Square Payments
    API is not being used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
