

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .letta_request_config import LettaRequestConfig
from .run_status import RunStatus
from .stop_reason_type import StopReasonType


class Run(UniversalBaseModel):
    """
    Representation of a run - a conversation or processing session for an agent. Runs track when agents process messages and maintain the relationship between agents, steps, and messages.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Run
    """

    status: typing.Optional[RunStatus] = pydantic.Field(default=None)
    """
    The current status of the run.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the run was created.
    """

    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the run was completed.
    """

    agent_id: str = pydantic.Field()
    """
    The unique identifier of the agent associated with the run.
    """

    conversation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the conversation associated with the run.
    """

    base_template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The base template ID that the run belongs to.
    """

    background: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the run was created in background mode.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional metadata for the run.
    """

    request_config: typing.Optional[LettaRequestConfig] = pydantic.Field(default=None)
    """
    The request configuration for the run.
    """

    stop_reason: typing.Optional[StopReasonType] = pydantic.Field(default=None)
    """
    The reason why the run was stopped.
    """

    callback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    If set, POST to this URL when the run completes.
    """

    callback_sent_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the callback was last attempted.
    """

    callback_status_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP status code returned by the callback endpoint.
    """

    callback_error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional error message from attempting to POST the callback endpoint.
    """

    ttft_ns: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time to first token for a run in nanoseconds
    """

    total_duration_ns: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total run duration in nanoseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
