

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecommerce_discount import EcommerceDiscount
from .ecommerce_order_line_item_options_item import EcommerceOrderLineItemOptionsItem
from .id import Id


class EcommerceOrderLineItem(UniversalBaseModel):
    """
    A single line item of an ecommerce order, representing a product or variant with associated options, quantity, and pricing information.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the product or variant associated with the line item.
    """

    discounts: typing.Optional[typing.List[EcommerceDiscount]] = None
    id: typing.Optional[Id] = None
    name: str = pydantic.Field()
    """
    The name of the product or variant associated with the line item.
    """

    options: typing.Optional[typing.List[EcommerceOrderLineItemOptionsItem]] = None
    product_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the product associated with the line item.
    """

    quantity: str = pydantic.Field()
    """
    The quantity of the product or variant associated with the line item.
    """

    sku: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SKU of the product or variant associated with the line item.
    """

    tax_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The total tax amount applied to the product or variant associated with the line item.
    """

    tax_rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax rate applied to the product or variant associated with the line item.
    """

    total_amount: str = pydantic.Field()
    """
    The total amount for the product(s) or variant associated with the line item, including taxes and discounts.
    """

    unit_price: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unit price of the product or variant associated with the line item.
    """

    variant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the variant of the product associated with the line item, if applicable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
