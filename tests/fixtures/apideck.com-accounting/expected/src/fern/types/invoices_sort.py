

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invoices_sort_by import InvoicesSortBy
from .sort_direction import SortDirection


class InvoicesSort(UniversalBaseModel):
    by: typing.Optional[InvoicesSortBy] = pydantic.Field(default=None)
    """
    The field on which to sort the Invoices
    """

    direction: typing.Optional[SortDirection] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
