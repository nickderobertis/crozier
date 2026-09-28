

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .load_scenario_list_entry_threshold_results_item_comparator import (
    LoadScenarioListEntryThresholdResultsItemComparator,
)
from .load_scenario_list_entry_threshold_results_item_metric import LoadScenarioListEntryThresholdResultsItemMetric


class LoadScenarioListEntryThresholdResultsItem(UniversalBaseModel):
    metric: typing.Optional[LoadScenarioListEntryThresholdResultsItemMetric] = None
    comparator: typing.Optional[LoadScenarioListEntryThresholdResultsItemComparator] = None
    threshold: typing.Optional[float] = None
    observed: typing.Optional[float] = pydantic.Field(default=None)
    """
    the observed per-run value at evaluation time (latency ms, error-rate fraction, or requests/second)
    """

    satisfied: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
