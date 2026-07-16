

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeleteInvoiceRequest(UniversalBaseModel):
    """
    Describes a `DeleteInvoice` request.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete.
    If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or 
    [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
