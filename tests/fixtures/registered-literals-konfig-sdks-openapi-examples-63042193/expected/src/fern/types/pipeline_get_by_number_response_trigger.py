

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_get_by_number_response_trigger_actor import PipelineGetByNumberResponseTriggerActor
from .pipeline_get_by_number_response_trigger_type import PipelineGetByNumberResponseTriggerType


class PipelineGetByNumberResponseTrigger(UniversalBaseModel):
    """
    A summary of the trigger.
    """

    type: PipelineGetByNumberResponseTriggerType = pydantic.Field()
    """
    The type of trigger.
    """

    received_at: dt.datetime = pydantic.Field()
    """
    The date and time the trigger was received.
    """

    actor: PipelineGetByNumberResponseTriggerActor = pydantic.Field()
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
