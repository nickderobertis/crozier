

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1money import V1Money
from .v1payment_discount import V1PaymentDiscount
from .v1payment_item_detail import V1PaymentItemDetail
from .v1payment_modifier import V1PaymentModifier
from .v1payment_tax import V1PaymentTax


class V1PaymentItemization(UniversalBaseModel):
    """
    Payment include an` itemizations` field that lists the items purchased,
    along with associated fees, modifiers, and discounts. Each itemization has an
    `itemization_type` field that indicates which of the following the itemization
    represents:

    <ul>
    <li>An item variation from the merchant's item library</li>
    <li>A custom monetary amount</li>
    <li>
    An action performed on a Square gift card, such as activating or
    reloading it.
    </li>
    </ul>

    *Note**: itemization information included in a `Payment` object reflects
    details collected **at the time of the payment**. Details such as the name or
    price of items might have changed since the payment was processed.
    """

    discount_money: typing.Optional[V1Money] = None
    discounts: typing.Optional[typing.List[V1PaymentDiscount]] = pydantic.Field(default=None)
    """
    All discounts applied to this itemization.
    """

    gross_sales_money: typing.Optional[V1Money] = None
    item_detail: typing.Optional[V1PaymentItemDetail] = None
    item_variation_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the item variation purchased, if any.
    """

    itemization_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of purchase that the itemization represents, such as an ITEM or CUSTOM_AMOUNT
    """

    modifiers: typing.Optional[typing.List[V1PaymentModifier]] = pydantic.Field(default=None)
    """
    All modifier options applied to this itemization.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item's name.
    """

    net_sales_money: typing.Optional[V1Money] = None
    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes entered by the merchant about the item at the time of payment, if any.
    """

    quantity: typing.Optional[float] = pydantic.Field(default=None)
    """
    The quantity of the item purchased. This can be a decimal value.
    """

    single_quantity_money: typing.Optional[V1Money] = None
    taxes: typing.Optional[typing.List[V1PaymentTax]] = pydantic.Field(default=None)
    """
    All taxes applied to this itemization.
    """

    total_money: typing.Optional[V1Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
