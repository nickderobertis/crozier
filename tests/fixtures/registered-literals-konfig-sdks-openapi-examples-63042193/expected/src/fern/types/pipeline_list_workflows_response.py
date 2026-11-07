

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_list_workflows_response_items_item import PipelineListWorkflowsResponseItemsItem


class PipelineListWorkflowsResponse(UniversalBaseModel):
    """
    A list of workflows and associated pagination token.
    """

    items: typing.List[PipelineListWorkflowsResponseItemsItem] = pydantic.Field()
    """
    A list of workflows.
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
