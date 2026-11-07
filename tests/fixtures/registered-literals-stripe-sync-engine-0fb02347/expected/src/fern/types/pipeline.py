

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destination_config import DestinationConfig
from .pipeline_desired_status import PipelineDesiredStatus
from .pipeline_status import PipelineStatus
from .pipeline_streams_item import PipelineStreamsItem
from .source_config import SourceConfig
from .sync_state import SyncState


class Pipeline(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique pipeline identifier (e.g. pipe_abc123).
    """

    source: SourceConfig
    destination: DestinationConfig
    streams: typing.Optional[typing.List[PipelineStreamsItem]] = pydantic.Field(default=None)
    """
    Selected streams to sync. All streams synced if omitted.
    """

    desired_status: PipelineDesiredStatus = pydantic.Field()
    """
    User-controlled lifecycle state. Set via PATCH to pause, resume, or delete.
    """

    status: PipelineStatus = pydantic.Field()
    """
    Workflow-controlled execution state. Updated by the Temporal workflow.
    """

    sync_state: typing.Optional[SyncState] = pydantic.Field(default=None)
    """
    Latest full sync checkpoint emitted by the engine. Includes source, destination, and sync-run state for the next request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
