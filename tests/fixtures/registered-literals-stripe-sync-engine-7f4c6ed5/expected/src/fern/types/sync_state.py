

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .source_state import SourceState
from .sync_state_sync_run import SyncStateSyncRun


class SyncState(UniversalBaseModel):
    """
    Full sync checkpoint with separate sections for source, destination, and sync run. Connectors only see their own section; the engine manages routing.
    """

    source: SourceState
    destination: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Destination connector state.
    """

    sync_run: SyncStateSyncRun = pydantic.Field()
    """
    Engine-managed run state — run_id, time_ceiling, accumulated progress.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
