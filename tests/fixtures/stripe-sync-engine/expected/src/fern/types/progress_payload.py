

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .progress_payload_connection_status import ProgressPayloadConnectionStatus
from .progress_payload_derived import ProgressPayloadDerived
from .stream_progress import StreamProgress


class ProgressPayload(UniversalBaseModel):
    """
    Periodic sync progress emitted by the engine as a top-level message. Each emission is a full replacement.
    """

    started_at: str = pydantic.Field()
    """
    When this sync started (ISO 8601); generally equals time_ceiling.
    """

    elapsed_ms: int = pydantic.Field()
    """
    Wall-clock milliseconds since the sync run started.
    """

    global_state_count: int = pydantic.Field()
    """
    Total source_state messages observed so far.
    """

    connection_status: typing.Optional[ProgressPayloadConnectionStatus] = pydantic.Field(default=None)
    """
    Set when source or destination emits connection_status: failed.
    """

    derived: ProgressPayloadDerived = pydantic.Field()
    """
    Computed aggregates.
    """

    streams: typing.Dict[str, StreamProgress] = pydantic.Field()
    """
    Per-stream progress, keyed by stream name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
