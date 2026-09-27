

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .load_scenario_report_threshold_results_item_comparator import LoadScenarioReportThresholdResultsItemComparator
from .load_scenario_report_threshold_results_item_metric import LoadScenarioReportThresholdResultsItemMetric


class LoadScenarioReportThresholdResultsItem(UniversalBaseModel):
    metric: typing.Optional[LoadScenarioReportThresholdResultsItemMetric] = None
    comparator: typing.Optional[LoadScenarioReportThresholdResultsItemComparator] = None
    threshold: typing.Optional[float] = None
    observed: typing.Optional[float] = None
    satisfied: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
