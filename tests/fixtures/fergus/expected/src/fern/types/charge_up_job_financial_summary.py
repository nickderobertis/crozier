

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .charge_up_job_financial_summary_chargeable_amount import ChargeUpJobFinancialSummaryChargeableAmount
from .charge_up_job_financial_summary_costs_incurred import ChargeUpJobFinancialSummaryCostsIncurred
from .charge_up_job_financial_summary_labour_hours import ChargeUpJobFinancialSummaryLabourHours
from .charge_up_job_financial_summary_total_billed import ChargeUpJobFinancialSummaryTotalBilled


class ChargeUpJobFinancialSummary(UniversalBaseModel):
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    job_no: typing_extensions.Annotated[str, FieldMetadata(alias="jobNo"), pydantic.Field(alias="jobNo")]
    last_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    currency: str
    costs_incurred: typing_extensions.Annotated[
        ChargeUpJobFinancialSummaryCostsIncurred,
        FieldMetadata(alias="costsIncurred"),
        pydantic.Field(alias="costsIncurred"),
    ]
    chargeable_amount: typing_extensions.Annotated[
        ChargeUpJobFinancialSummaryChargeableAmount,
        FieldMetadata(alias="chargeableAmount"),
        pydantic.Field(alias="chargeableAmount"),
    ]
    total_billed: typing_extensions.Annotated[
        ChargeUpJobFinancialSummaryTotalBilled, FieldMetadata(alias="totalBilled"), pydantic.Field(alias="totalBilled")
    ]
    labour_hours: typing_extensions.Annotated[
        ChargeUpJobFinancialSummaryLabourHours, FieldMetadata(alias="labourHours"), pydantic.Field(alias="labourHours")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
