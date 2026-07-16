

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvoiceCustomField(UniversalBaseModel):
    """
    An additional seller-defined and customer-facing field to include on the invoice. For more information,
    see [Custom fields](https://developer.squareup.com/docs/invoices-api/overview#custom-fields).

    Adding custom fields to an invoice requires an
    [Invoices Plus subscription](https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription).
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label or title of the custom field. This field is required for a custom field.
    """

    placement: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location of the custom field on the invoice. This field is required for a custom field.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the custom field. If omitted, only the label is rendered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
