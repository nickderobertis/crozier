

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_financial_summary_one_chargeable_amount import JobFinancialSummaryOneChargeableAmount
from .job_financial_summary_one_costs_incurred import JobFinancialSummaryOneCostsIncurred
from .job_financial_summary_one_job_type import JobFinancialSummaryOneJobType
from .job_financial_summary_one_labour_hours import JobFinancialSummaryOneLabourHours
from .job_financial_summary_one_total_billed import JobFinancialSummaryOneTotalBilled


class JobFinancialSummaryOne(UniversalBaseModel):
    job_type: typing_extensions.Annotated[
        JobFinancialSummaryOneJobType, FieldMetadata(alias="jobType"), pydantic.Field(alias="jobType")
    ]
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    job_no: typing_extensions.Annotated[str, FieldMetadata(alias="jobNo"), pydantic.Field(alias="jobNo")]
    last_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    currency: str
    costs_incurred: typing_extensions.Annotated[
        JobFinancialSummaryOneCostsIncurred, FieldMetadata(alias="costsIncurred"), pydantic.Field(alias="costsIncurred")
    ]
    chargeable_amount: typing_extensions.Annotated[
        JobFinancialSummaryOneChargeableAmount,
        FieldMetadata(alias="chargeableAmount"),
        pydantic.Field(alias="chargeableAmount"),
    ]
    total_billed: typing_extensions.Annotated[
        JobFinancialSummaryOneTotalBilled, FieldMetadata(alias="totalBilled"), pydantic.Field(alias="totalBilled")
    ]
    labour_hours: typing_extensions.Annotated[
        JobFinancialSummaryOneLabourHours, FieldMetadata(alias="labourHours"), pydantic.Field(alias="labourHours")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
