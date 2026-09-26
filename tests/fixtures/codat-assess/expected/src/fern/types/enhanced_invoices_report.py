

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .enhanced_invoices_report_report_items_item import EnhancedInvoicesReportReportItemsItem


class EnhancedInvoicesReport(UniversalBaseModel):
    """
    The enhanced invoices report takes the key elements of the Invoices report verifying those marked as paid in the accounting platform have actually been paid by matching with the bank statement.
    """

    report_info: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="reportInfo"), pydantic.Field(alias="reportInfo")
    ] = None
    report_items: typing_extensions.Annotated[
        typing.Optional[typing.List[EnhancedInvoicesReportReportItemsItem]],
        FieldMetadata(alias="reportItems"),
        pydantic.Field(alias="reportItems"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
