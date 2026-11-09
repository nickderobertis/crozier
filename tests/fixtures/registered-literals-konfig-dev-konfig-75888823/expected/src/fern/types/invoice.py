

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .invoice_status import InvoiceStatus


class Invoice(UniversalBaseModel):
    status: InvoiceStatus
    amount_due: typing_extensions.Annotated[float, FieldMetadata(alias="amountDue"), pydantic.Field(alias="amountDue")]
    pdf_url: typing_extensions.Annotated[str, FieldMetadata(alias="pdfUrl"), pydantic.Field(alias="pdfUrl")]
    due_date: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="dueDate"), pydantic.Field(alias="dueDate")]
    year: float
    month: float
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
