

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .amount import Amount
from .invoice_item_group import InvoiceItemGroup
from .label_monetary_account import LabelMonetaryAccount


class InvoiceByUserRead(UniversalBaseModel):
    address: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The customer's address.
    """

    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The label that's displayed to the counterparty with the invoice. Includes user.
    """

    chamber_of_commerce_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's chamber of commerce number.
    """

    counterparty_address: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The company's address.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The label of the counterparty of the invoice. Includes user.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the invoice object's creation.
    """

    group: typing.Optional[typing.List[InvoiceItemGroup]] = pydantic.Field(default=None)
    """
    The invoice item groups.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the invoice object.
    """

    invoice_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The invoice date.
    """

    invoice_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The invoice number.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The invoice status.
    """

    total_vat: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The VAT on the total discounted item price.
    """

    total_vat_exclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total discounted item price excluding VAT.
    """

    total_vat_inclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total discounted item price including VAT.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the invoice object's last update.
    """

    vat_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's chamber of commerce number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
