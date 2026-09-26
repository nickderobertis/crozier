

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message import Message
from .run_create_config import RunCreateConfig
from .run_create_if_not_exists import RunCreateIfNotExists
from .run_create_input import RunCreateInput
from .run_create_on_completion import RunCreateOnCompletion
from .run_create_on_disconnect import RunCreateOnDisconnect


class RunCreate(UniversalBaseModel):
    """
    Payload for creating a run.
    """

    thread_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the thread to run. If not provided, creates a stateless run. 'thread_id' is ignored unless Threads stage is implemented.
    """

    agent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The agent ID to run. If not provided will use the default agent for this service. 'agent_id' is ignored unless Agents stage is implemented.
    """

    input: typing.Optional[RunCreateInput] = pydantic.Field(default=None)
    """
    The input to the agent.
    """

    messages: typing.Optional[typing.List[Message]] = pydantic.Field(default=None)
    """
    The messages to pass an input to the agent.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Metadata to assign to the run.
    """

    config: typing.Optional[RunCreateConfig] = pydantic.Field(default=None)
    """
    The configuration for the agent.
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    Webhook to call after run finishes.
    """

    on_completion: typing.Optional[RunCreateOnCompletion] = pydantic.Field(default=None)
    """
    Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.
    """

    on_disconnect: typing.Optional[RunCreateOnDisconnect] = pydantic.Field(default=None)
    """
    The disconnect mode to use. Must be one of 'cancel' or 'continue'.
    """

    if_not_exists: typing.Optional[RunCreateIfNotExists] = pydantic.Field(default=None)
    """
    How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
