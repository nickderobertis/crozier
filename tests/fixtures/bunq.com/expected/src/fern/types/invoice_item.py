

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class InvoiceItem(UniversalBaseModel):
    billing_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The billing date of the item.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the invoice item.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of items priced.
    """

    total_vat_exclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The item price excluding VAT.
    """

    total_vat_inclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The item price including VAT.
    """

    type_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The price description.
    """

    type_description_translated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The translated price description.
    """

    unit_vat_exclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The unit item price excluding VAT.
    """

    unit_vat_inclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The unit item price including VAT.
    """

    vat: typing.Optional[int] = pydantic.Field(default=None)
    """
    The VAT tax fraction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
