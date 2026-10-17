

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checkpoint_config import CheckpointConfig
from .command import Command
from .run_create_stateful_config import RunCreateStatefulConfig
from .run_create_stateful_durability import RunCreateStatefulDurability
from .run_create_stateful_if_not_exists import RunCreateStatefulIfNotExists
from .run_create_stateful_input import RunCreateStatefulInput
from .run_create_stateful_interrupt_after import RunCreateStatefulInterruptAfter
from .run_create_stateful_interrupt_before import RunCreateStatefulInterruptBefore
from .run_create_stateful_multitask_strategy import RunCreateStatefulMultitaskStrategy
from .run_create_stateful_stream_mode import RunCreateStatefulStreamMode


class RunCreateStateful(UniversalBaseModel):
    """
    Payload for creating a run.
    """

    assistant_id: str
    checkpoint: typing.Optional[CheckpointConfig] = pydantic.Field(default=None)
    """
    The checkpoint to resume from.
    """

    input: typing.Optional[RunCreateStatefulInput] = pydantic.Field(default=None)
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

    config: typing.Optional[RunCreateStatefulConfig] = pydantic.Field(default=None)
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

    interrupt_before: typing.Optional[RunCreateStatefulInterruptBefore] = pydantic.Field(default=None)
    """
    Nodes to interrupt immediately before they get executed.
    """

    interrupt_after: typing.Optional[RunCreateStatefulInterruptAfter] = pydantic.Field(default=None)
    """
    Nodes to interrupt immediately after they get executed.
    """

    stream_mode: typing.Optional[RunCreateStatefulStreamMode] = pydantic.Field(default=None)
    """
    The stream mode(s) to use.
    """

    stream_subgraphs: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to stream output from subgraphs.
    """

    stream_resumable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to persist the stream chunks in order to resume the stream later.
    """

    feedback_keys: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Generate pre-signed URLs for assigning feedback keys to the run.
    
    For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.
    """

    multitask_strategy: typing.Optional[RunCreateStatefulMultitaskStrategy] = pydantic.Field(default=None)
    """
    Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.
    """

    if_not_exists: typing.Optional[RunCreateStatefulIfNotExists] = pydantic.Field(default=None)
    """
    How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).
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

    durability: typing.Optional[RunCreateStatefulDurability] = pydantic.Field(default=None)
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
