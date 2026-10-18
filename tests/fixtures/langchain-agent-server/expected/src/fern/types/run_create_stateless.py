

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .command import Command
from .run_create_stateless_config import RunCreateStatelessConfig
from .run_create_stateless_durability import RunCreateStatelessDurability
from .run_create_stateless_input import RunCreateStatelessInput
from .run_create_stateless_on_completion import RunCreateStatelessOnCompletion
from .run_create_stateless_stream_mode import RunCreateStatelessStreamMode


class RunCreateStateless(UniversalBaseModel):
    """
    Payload for creating a run.
    """

    assistant_id: str
    input: typing.Optional[RunCreateStatelessInput] = pydantic.Field(default=None)
    """
    The input to the graph.
    """

    command: typing.Optional[Command] = pydantic.Field(default=None)
    """
    The input to the graph.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Metadata to assign to the run.
    """

    config: typing.Optional[RunCreateStatelessConfig] = pydantic.Field(default=None)
    """
    The configuration for the assistant.
    """

    context: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Static context added to the assistant.
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    Webhook to call after LangGraph API call is done.
    """

    stream_mode: typing.Optional[RunCreateStatelessStreamMode] = pydantic.Field(default=None)
    """
    The stream mode(s) to use.
    """

    feedback_keys: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Generate pre-signed URLs for assigning feedback keys to the run.
    
    For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.
    """

    stream_subgraphs: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to stream output from subgraphs.
    """

    stream_resumable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to persist the stream chunks in order to resume the stream later.
    """

    on_completion: typing.Optional[RunCreateStatelessOnCompletion] = pydantic.Field(default=None)
    """
    Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.
    """

    after_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of seconds to wait before starting the run. Use to schedule future runs.
    """

    checkpoint_during: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to checkpoint during the run.
    
    Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.
    """

    durability: typing.Optional[RunCreateStatelessDurability] = pydantic.Field(default=None)
    """
    Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
