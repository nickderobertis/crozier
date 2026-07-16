

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invoice_filter import InvoiceFilter
from .invoice_sort import InvoiceSort


class InvoiceQuery(UniversalBaseModel):
    """
    Describes query criteria for searching invoices.
    """

    filter: InvoiceFilter
    sort: typing.Optional[InvoiceSort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
