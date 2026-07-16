

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class GiftCardActivityLoad(UniversalBaseModel):
    """
    Present only when `GiftCardActivityType` is LOAD.
    """

    amount_money: typing.Optional[Money] = None
    buyer_payment_instrument_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    If you are not using the Orders API, this field is required because it is used to identify a buyer 
    to perform compliance checks.
    """

    line_item_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `line_item_uid` of the gift card’s line item in the order associated with the activity.
    It is populated along with `order_id` and is required if using the Square Orders API.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `order_id` of the order associated with the activity.
    It is populated along with `line_item_uid` and is required if using the Square Orders API.
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
