

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Product(UniversalBaseModel):
    """
    Product details associated with a transaction.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Product name.
    """

    price_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable label for the product price.
    """

    price: typing.Optional[float] = pydantic.Field(default=None)
    """
    Product price.
    """

    vat_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    VAT rate applied to the product price.
    """

    single_vat_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    VAT amount for a single product.
    """

    price_with_vat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Product price including VAT.
    """

    vat_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total VAT amount for the product quantity.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    Product quantity.
    """

    total_price: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total price calculated as the product price multiplied by the quantity.
    """

    total_with_vat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total product price including VAT.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
