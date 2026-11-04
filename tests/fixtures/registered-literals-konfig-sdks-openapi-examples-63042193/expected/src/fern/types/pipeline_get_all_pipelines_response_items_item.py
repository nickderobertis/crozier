

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_get_all_pipelines_response_items_item_errors_item import (
    PipelineGetAllPipelinesResponseItemsItemErrorsItem,
)
from .pipeline_get_all_pipelines_response_items_item_state import PipelineGetAllPipelinesResponseItemsItemState
from .pipeline_get_all_pipelines_response_items_item_trigger import PipelineGetAllPipelinesResponseItemsItemTrigger
from .pipeline_get_all_pipelines_response_items_item_trigger_parameters_value import (
    PipelineGetAllPipelinesResponseItemsItemTriggerParametersValue,
)
from .pipeline_get_all_pipelines_response_items_item_vcs import PipelineGetAllPipelinesResponseItemsItemVcs


class PipelineGetAllPipelinesResponseItemsItem(UniversalBaseModel):
    """
    A pipeline response.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the pipeline.
    """

    errors: typing.List[PipelineGetAllPipelinesResponseItemsItemErrorsItem] = pydantic.Field()
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
        typing.Dict[str, PipelineGetAllPipelinesResponseItemsItemTriggerParametersValue]
    ] = None
    state: PipelineGetAllPipelinesResponseItemsItemState = pydantic.Field()
    """
    The current state of the pipeline.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the pipeline was created.
    """

    trigger: PipelineGetAllPipelinesResponseItemsItemTrigger = pydantic.Field()
    """
    A summary of the trigger.
    """

    vcs: typing.Optional[PipelineGetAllPipelinesResponseItemsItemVcs] = pydantic.Field(default=None)
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
