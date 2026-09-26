

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1forecast_summary_estimated_total import V1ForecastSummaryEstimatedTotal
from .v1forecast_summary_logged_total import V1ForecastSummaryLoggedTotal
from .v1forecast_summary_planned_total import V1ForecastSummaryPlannedTotal


class V1ForecastSummary(UniversalBaseModel):
    task_count: int = pydantic.Field()
    """
    Number of tasks matching the filter
    """

    estimated_total: V1ForecastSummaryEstimatedTotal = pydantic.Field()
    """
    Total estimated duration
    """

    logged_total: V1ForecastSummaryLoggedTotal = pydantic.Field()
    """
    Total logged duration
    """

    planned_total: V1ForecastSummaryPlannedTotal = pydantic.Field()
    """
    Total planned duration
    """

    due_dates: typing.List[str] = pydantic.Field()
    """
    List of due dates
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    User ID (present for user summaries)
    """

    project_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Project ID (present for project summaries)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
