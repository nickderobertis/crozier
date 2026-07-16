

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogTax(UniversalBaseModel):
    """
    A tax applicable to an item.
    """

    applies_to_custom_amounts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the fee applies to custom amounts entered into the Square Point of Sale
    app that are not associated with a particular `CatalogItem`.
    """

    calculation_phase: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the tax is calculated based on a payment's subtotal or total.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A Boolean flag to indicate whether the tax is displayed as enabled (`true`) in the Square Point of Sale app or not (`false`).
    """

    inclusion_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the tax is `ADDITIVE` or `INCLUSIVE`.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax's name. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    """

    percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The percentage of the tax in decimal form, using a `'.'` as the decimal separator and without a `'%'` sign.
    A value of `7.5` corresponds to 7.5%.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
