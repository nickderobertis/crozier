

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class CatalogDiscount(UniversalBaseModel):
    """
    A discount applicable to items.
    """

    amount_money: typing.Optional[Money] = None
    discount_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether the discount is a fixed amount or percentage, or entered at the time of sale.
    """

    label_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The color of the discount display label in the Square Point of Sale app. This must be a valid hex color code.
    """

    modify_tax_basis: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether this discount should reduce the price used to calculate tax.
    
    Most discounts should use `MODIFY_TAX_BASIS`. However, in some circumstances taxes must
    be calculated based on an item's price, ignoring a particular discount. For example,
    in many US jurisdictions, a manufacturer coupon or instant rebate reduces the price a
    customer pays but does not reduce the sale price used to calculate how much sales tax is
    due. In this case, the discount representing that manufacturer coupon should have
    `DO_NOT_MODIFY_TAX_BASIS` for this field.
    
    If you are unsure whether you need to use this field, consult your tax professional.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The discount name. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    """

    percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The percentage of the discount as a string representation of a decimal number, using a `.` as the decimal
    separator and without a `%` sign. A value of `7.5` corresponds to `7.5%`. Specify a percentage of `0` if `discount_type`
    is `VARIABLE_PERCENTAGE`.
    
    Do not use this field for amount-based or variable discounts.
    """

    pin_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether a mobile staff member needs to enter their PIN to apply the
    discount to a payment in the Square Point of Sale app.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
