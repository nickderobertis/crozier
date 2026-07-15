

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .linked_tax_rate import LinkedTaxRate
from .tax_inclusive import TaxInclusive
from .unit_of_measure import UnitOfMeasure
from .unit_price import UnitPrice


class InvoiceItemSalesDetails(UniversalBaseModel):
    tax_inclusive: typing.Optional[TaxInclusive] = None
    tax_rate: typing.Optional[LinkedTaxRate] = None
    unit_of_measure: typing.Optional[UnitOfMeasure] = None
    unit_price: typing.Optional[UnitPrice] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
