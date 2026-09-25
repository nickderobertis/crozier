

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_financial_summary_quote_summary_chargeable_amount import JobFinancialSummaryQuoteSummaryChargeableAmount
from .job_financial_summary_quote_summary_costs_incurred import JobFinancialSummaryQuoteSummaryCostsIncurred
from .job_financial_summary_quote_summary_job_type import JobFinancialSummaryQuoteSummaryJobType
from .job_financial_summary_quote_summary_labour_hours import JobFinancialSummaryQuoteSummaryLabourHours
from .job_financial_summary_quote_summary_quote_summary import JobFinancialSummaryQuoteSummaryQuoteSummary
from .job_financial_summary_quote_summary_total_billed import JobFinancialSummaryQuoteSummaryTotalBilled


class JobFinancialSummaryQuoteSummary(UniversalBaseModel):
    job_type: typing_extensions.Annotated[
        JobFinancialSummaryQuoteSummaryJobType, FieldMetadata(alias="jobType"), pydantic.Field(alias="jobType")
    ]
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    job_no: typing_extensions.Annotated[str, FieldMetadata(alias="jobNo"), pydantic.Field(alias="jobNo")]
    last_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    currency: str
    costs_incurred: typing_extensions.Annotated[
        JobFinancialSummaryQuoteSummaryCostsIncurred,
        FieldMetadata(alias="costsIncurred"),
        pydantic.Field(alias="costsIncurred"),
    ]
    chargeable_amount: typing_extensions.Annotated[
        JobFinancialSummaryQuoteSummaryChargeableAmount,
        FieldMetadata(alias="chargeableAmount"),
        pydantic.Field(alias="chargeableAmount"),
    ]
    total_billed: typing_extensions.Annotated[
        JobFinancialSummaryQuoteSummaryTotalBilled,
        FieldMetadata(alias="totalBilled"),
        pydantic.Field(alias="totalBilled"),
    ]
    labour_hours: typing_extensions.Annotated[
        JobFinancialSummaryQuoteSummaryLabourHours,
        FieldMetadata(alias="labourHours"),
        pydantic.Field(alias="labourHours"),
    ]
    quote_summary: typing_extensions.Annotated[
        JobFinancialSummaryQuoteSummaryQuoteSummary,
        FieldMetadata(alias="quoteSummary"),
        pydantic.Field(alias="quoteSummary"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
