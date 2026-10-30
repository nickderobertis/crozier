

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_details import PipelineDetails
from .running_state import RunningState


class ComputationGet(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    the id of the computation task
    """

    state: RunningState = pydantic.Field()
    """
    the state of the computational task
    """

    result: typing.Optional[str] = pydantic.Field(default=None)
    """
    the result of the computational task
    """

    pipeline_details: PipelineDetails = pydantic.Field()
    """
    the details of the generated pipeline
    """

    iteration: typing.Optional[int] = pydantic.Field(default=None)
    """
    the iteration id of the computation task (none if no task ran yet)
    """

    started: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    the timestamp when the computation was started or None if not started yet
    """

    stopped: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    the timestamp when the computation was stopped or None if not started nor stopped yet
    """

    submitted: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    task last modification timestamp or None if the there is no task
    """

    url: str = pydantic.Field()
    """
    the link where to get the status of the task
    """

    stop_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    the link where to stop the task
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
