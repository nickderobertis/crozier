

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .invoice_item import InvoiceItem


class InvoiceItemGroup(UniversalBaseModel):
    instance_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the invoice item group.
    """

    item: typing.Optional[typing.List[InvoiceItem]] = pydantic.Field(default=None)
    """
    The invoice items in the group.
    """

    product_vat_exclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The unit item price excluding VAT.
    """

    product_vat_inclusive: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The unit item price including VAT.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the invoice item group.
    """

    type_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the type of the invoice item group.
    """

    type_description_translated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The translated description of the type of the invoice item group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
