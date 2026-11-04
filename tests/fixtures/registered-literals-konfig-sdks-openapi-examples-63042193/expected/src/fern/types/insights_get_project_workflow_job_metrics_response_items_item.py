

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_workflow_job_metrics_response_items_item_metrics import (
    InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics,
)


class InsightsGetProjectWorkflowJobMetricsResponseItemsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the job.
    """

    metrics: InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics = pydantic.Field()
    """
    Metrics relating to a workflow job's runs.
    """

    window_start: dt.datetime = pydantic.Field()
    """
    The timestamp of the first build within the requested reporting window.
    """

    window_end: dt.datetime = pydantic.Field()
    """
    The timestamp of the last build within the requested reporting window.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
