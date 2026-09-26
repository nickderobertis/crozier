

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .detailed_customer_invoice_customer import DetailedCustomerInvoiceCustomer
from .detailed_customer_invoice_due_days import DetailedCustomerInvoiceDueDays
from .detailed_customer_invoice_sections_item import DetailedCustomerInvoiceSectionsItem
from .detailed_customer_invoice_status import DetailedCustomerInvoiceStatus
from .detailed_customer_invoice_type import DetailedCustomerInvoiceType
from .links import Links


class DetailedCustomerInvoice(UniversalBaseModel):
    id: float
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    customer_id: typing_extensions.Annotated[
        float, FieldMetadata(alias="customerId"), pydantic.Field(alias="customerId")
    ]
    attn: typing.Optional[str] = None
    title: str
    description: typing.Optional[str] = None
    invoice_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invoiceNumber"), pydantic.Field(alias="invoiceNumber")
    ] = None
    receiver_email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="receiverEmail"), pydantic.Field(alias="receiverEmail")
    ] = None
    receiver_full_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="receiverFullName"), pydantic.Field(alias="receiverFullName")
    ] = None
    receiver_postal_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="receiverPostalAddress"),
        pydantic.Field(alias="receiverPostalAddress"),
    ] = None
    due_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dueDate"), pydantic.Field(alias="dueDate")
    ] = None
    due_days: typing_extensions.Annotated[
        typing.Optional[DetailedCustomerInvoiceDueDays],
        FieldMetadata(alias="dueDays"),
        pydantic.Field(
            alias="dueDays",
            description="Number of days or one of '20th_of_next_month', '20th_of_current_month', 'last_day_of_current_month', 'last_day_of_next_month', 'use_default'",
        ),
    ] = None
    """
    Number of days or one of '20th_of_next_month', '20th_of_current_month', 'last_day_of_current_month', 'last_day_of_next_month', 'use_default'
    """

    invoice_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="invoiceDate"), pydantic.Field(alias="invoiceDate")
    ] = None
    paid_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="paidAt"), pydantic.Field(alias="paidAt")
    ] = None
    subtotal: float
    tax_value: typing_extensions.Annotated[float, FieldMetadata(alias="taxValue"), pydantic.Field(alias="taxValue")]
    total_paid: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="totalPaid"), pydantic.Field(alias="totalPaid")
    ] = None
    tax_rate: typing_extensions.Annotated[float, FieldMetadata(alias="taxRate"), pydantic.Field(alias="taxRate")]
    type: DetailedCustomerInvoiceType
    status: DetailedCustomerInvoiceStatus
    is_sent: typing_extensions.Annotated[bool, FieldMetadata(alias="isSent"), pydantic.Field(alias="isSent")]
    is_final: typing_extensions.Annotated[bool, FieldMetadata(alias="isFinal"), pydantic.Field(alias="isFinal")]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    fergus_pay_enabled: typing_extensions.Annotated[
        bool, FieldMetadata(alias="fergusPayEnabled"), pydantic.Field(alias="fergusPayEnabled")
    ]
    links: typing.List[Links]
    customer: DetailedCustomerInvoiceCustomer
    sections: typing.List[DetailedCustomerInvoiceSectionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DetailedCustomerInvoice)
