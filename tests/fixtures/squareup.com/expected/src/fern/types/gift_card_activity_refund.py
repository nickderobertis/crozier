

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class GiftCardActivityRefund(UniversalBaseModel):
    """
    Present only when `GiftCardActivityType` is REFUND.
    """

    amount_money: typing.Optional[Money] = None
    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    When the Square Payments API is used, Refund is not called on the Gift Cards API.
    However, when Square reads a Refund activity from the Gift Cards API, the developer needs to know the
    ID of the payment (made using this gift card) that is being refunded.
    """

    redeem_activity_id: str = pydantic.Field()
    """
    The ID for the Redeem activity that needs to be refunded. Hence, the activity it
    refers to has to be of the REDEEM type.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A client-specified ID to associate an entity, in another system, with this gift card
    activity. This can be used to track the order or payment related information when the Square Orders
    API is not being used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
