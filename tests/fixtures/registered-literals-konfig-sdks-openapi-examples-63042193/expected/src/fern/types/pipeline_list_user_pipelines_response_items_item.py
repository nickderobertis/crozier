

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_list_user_pipelines_response_items_item_errors_item import (
    PipelineListUserPipelinesResponseItemsItemErrorsItem,
)
from .pipeline_list_user_pipelines_response_items_item_state import PipelineListUserPipelinesResponseItemsItemState
from .pipeline_list_user_pipelines_response_items_item_trigger import PipelineListUserPipelinesResponseItemsItemTrigger
from .pipeline_list_user_pipelines_response_items_item_trigger_parameters_value import (
    PipelineListUserPipelinesResponseItemsItemTriggerParametersValue,
)
from .pipeline_list_user_pipelines_response_items_item_vcs import PipelineListUserPipelinesResponseItemsItemVcs


class PipelineListUserPipelinesResponseItemsItem(UniversalBaseModel):
    """
    A pipeline response.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the pipeline.
    """

    errors: typing.List[PipelineListUserPipelinesResponseItemsItemErrorsItem] = pydantic.Field()
    """
    A sequence of errors that have occurred within the pipeline.
    """

    project_slug: str = pydantic.Field()
    """
    The project-slug for the pipeline.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the pipeline was last updated.
    """

    number: int = pydantic.Field()
    """
    The number of the pipeline.
    """

    trigger_parameters: typing.Optional[
        typing.Dict[str, PipelineListUserPipelinesResponseItemsItemTriggerParametersValue]
    ] = None
    state: PipelineListUserPipelinesResponseItemsItemState = pydantic.Field()
    """
    The current state of the pipeline.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the pipeline was created.
    """

    trigger: PipelineListUserPipelinesResponseItemsItemTrigger = pydantic.Field()
    """
    A summary of the trigger.
    """

    vcs: typing.Optional[PipelineListUserPipelinesResponseItemsItemVcs] = pydantic.Field(default=None)
    """
    VCS information for the pipeline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
