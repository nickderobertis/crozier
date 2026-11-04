

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_recent_workflow_runs_response_items_item import InsightsGetRecentWorkflowRunsResponseItemsItem


class InsightsGetRecentWorkflowRunsResponse(UniversalBaseModel):
    """
    Paginated recent workflow runs.
    """

    items: typing.List[InsightsGetRecentWorkflowRunsResponseItemsItem] = pydantic.Field()
    """
    Recent workflow runs.
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
