

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_trigger_new_pipeline_response_state import PipelineTriggerNewPipelineResponseState


class PipelineTriggerNewPipelineResponse(UniversalBaseModel):
    """
    A pipeline creation response.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the pipeline.
    """

    state: PipelineTriggerNewPipelineResponseState = pydantic.Field()
    """
    The current state of the pipeline.
    """

    number: int = pydantic.Field()
    """
    The number of the pipeline.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the pipeline was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
