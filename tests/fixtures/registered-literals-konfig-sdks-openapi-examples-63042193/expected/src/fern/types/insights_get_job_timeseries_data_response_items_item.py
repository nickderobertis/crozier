

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_job_timeseries_data_response_items_item_metrics import (
    InsightsGetJobTimeseriesDataResponseItemsItemMetrics,
)


class InsightsGetJobTimeseriesDataResponseItemsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the workflow.
    """

    min_started_at: dt.datetime = pydantic.Field()
    """
    The start time for the earliest execution included in the metrics.
    """

    max_ended_at: dt.datetime = pydantic.Field()
    """
    The end time of the last execution included in the metrics.
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    The start of the interval for timeseries metrics.
    """

    metrics: InsightsGetJobTimeseriesDataResponseItemsItemMetrics = pydantic.Field()
    """
    Metrics relating to a workflow's runs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
