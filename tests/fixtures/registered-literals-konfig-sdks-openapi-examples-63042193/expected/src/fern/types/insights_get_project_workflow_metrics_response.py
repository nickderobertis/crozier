

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_workflow_metrics_response_items_item import (
    InsightsGetProjectWorkflowMetricsResponseItemsItem,
)


class InsightsGetProjectWorkflowMetricsResponse(UniversalBaseModel):
    """
    Paginated workflow summary metrics.
    """

    items: typing.List[InsightsGetProjectWorkflowMetricsResponseItemsItem] = pydantic.Field()
    """
    Workflow summary metrics.
    """

    next_page_token: str = pydantic.Field()
    """
    A token to pass as a `page-token` query parameter to return the next page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
