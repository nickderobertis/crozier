

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .invoices_query_parameters_sort_field import InvoicesQueryParametersSortField
from .invoices_query_parameters_sort_order import InvoicesQueryParametersSortOrder


class InvoicesQueryParameters(UniversalBaseModel):
    page_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[InvoicesQueryParametersSortOrder],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder"),
    ] = None
    page_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageCursor"), pydantic.Field(alias="pageCursor")
    ] = None
    sort_field: typing_extensions.Annotated[
        typing.Optional[InvoicesQueryParametersSortField],
        FieldMetadata(alias="sortField"),
        pydantic.Field(alias="sortField"),
    ] = None
    customer_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="customerId"),
        pydantic.Field(alias="customerId", description="Filter by customer ID"),
    ] = None
    """
    Filter by customer ID
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="jobId"),
        pydantic.Field(alias="jobId", description="Filter by job ID"),
    ] = None
    """
    Filter by job ID
    """

    invoice_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="invoiceNumber"),
        pydantic.Field(alias="invoiceNumber", description="Search by invoiceNumber"),
    ] = None
    """
    Search by invoiceNumber
    """

    due_before: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dueBefore"),
        pydantic.Field(alias="dueBefore", description="Filter invoices due before this datetime"),
    ] = None
    """
    Filter invoices due before this datetime
    """

    due_after: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dueAfter"),
        pydantic.Field(alias="dueAfter", description="Filter invoices due after this datetime"),
    ] = None
    """
    Filter invoices due after this datetime
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
