

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class GiftCardActivityActivate(UniversalBaseModel):
    """
    Describes a gift card activity of the ACTIVATE type.
    """

    amount_money: typing.Optional[Money] = None
    buyer_payment_instrument_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Required if your application does not use the Square Orders API. 
    This is a list of client-provided payment instrument IDs. 
    Square uses this information to perform compliance checks.
    If you use the Square Orders API, Square has the necessary instrument IDs to perform necessary 
    compliance checks.
    """

    line_item_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `line_item_uid` of the gift card line item in an order. 
    This is required if your application uses the Square Orders API.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the order associated with the activity. 
    This is required if your application uses the Square Orders API.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If your application does not use the Square Orders API, you can optionally use this field 
    to associate the gift card activity with a client-side entity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
