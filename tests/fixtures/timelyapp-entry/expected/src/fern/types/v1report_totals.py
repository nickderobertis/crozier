

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1report_totals_billable_duration import V1ReportTotalsBillableDuration
from .v1report_totals_billed_cost import V1ReportTotalsBilledCost
from .v1report_totals_billed_duration import V1ReportTotalsBilledDuration
from .v1report_totals_cost import V1ReportTotalsCost
from .v1report_totals_duration import V1ReportTotalsDuration
from .v1report_totals_estimated_cost import V1ReportTotalsEstimatedCost
from .v1report_totals_estimated_duration import V1ReportTotalsEstimatedDuration
from .v1report_totals_internal_cost import V1ReportTotalsInternalCost
from .v1report_totals_non_billable_duration import V1ReportTotalsNonBillableDuration
from .v1report_totals_profit import V1ReportTotalsProfit
from .v1report_totals_unbilled_cost import V1ReportTotalsUnbilledCost
from .v1report_totals_unbilled_duration import V1ReportTotalsUnbilledDuration


class V1ReportTotals(UniversalBaseModel):
    id: int
    name: str
    projects: typing.List[typing.Any]
    duration: V1ReportTotalsDuration
    estimated_duration: V1ReportTotalsEstimatedDuration
    billed_duration: V1ReportTotalsBilledDuration
    unbilled_duration: V1ReportTotalsUnbilledDuration
    billable_duration: V1ReportTotalsBillableDuration
    non_billable_duration: V1ReportTotalsNonBillableDuration
    cost: V1ReportTotalsCost
    estimated_cost: V1ReportTotalsEstimatedCost
    billed_cost: V1ReportTotalsBilledCost
    unbilled_cost: V1ReportTotalsUnbilledCost
    internal_cost: V1ReportTotalsInternalCost
    profit: V1ReportTotalsProfit
    profitability: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
