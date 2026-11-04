

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_status import RunStatus


class WorkflowRunAttempt(UniversalBaseModel):
    attempt_number: int = pydantic.Field()
    """
    One-based number of this workflow run attempt
    """

    status: RunStatus = pydantic.Field()
    """
    Status of this workflow run attempt
    """

    failure_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason for failure, if the attempt failed
    """

    error_codes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Error codes reported by this attempt
    """

    started_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when this attempt started
    """

    finished_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when this attempt finished
    """

    retry_decision: typing.Optional[str] = pydantic.Field(default=None)
    """
    Retry decision recorded for this attempt
    """

    decision_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason recorded for the retry decision
    """

    next_attempt_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the next attempt is scheduled
    """

    webhook_sent_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the webhook for this attempt was sent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
