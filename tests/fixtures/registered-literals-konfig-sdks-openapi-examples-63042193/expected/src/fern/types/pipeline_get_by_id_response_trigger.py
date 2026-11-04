

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_get_by_id_response_trigger_actor import PipelineGetByIdResponseTriggerActor
from .pipeline_get_by_id_response_trigger_type import PipelineGetByIdResponseTriggerType


class PipelineGetByIdResponseTrigger(UniversalBaseModel):
    """
    A summary of the trigger.
    """

    type: PipelineGetByIdResponseTriggerType = pydantic.Field()
    """
    The type of trigger.
    """

    received_at: dt.datetime = pydantic.Field()
    """
    The date and time the trigger was received.
    """

    actor: PipelineGetByIdResponseTriggerActor = pydantic.Field()
    """
    The user who triggered the Pipeline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
