

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fleet_ui_message_chunk_data_child_progress_data_cleanup_state import (
    FleetUiMessageChunkDataChildProgressDataCleanupState,
)
from .fleet_ui_message_chunk_data_child_progress_data_state import FleetUiMessageChunkDataChildProgressDataState


class FleetUiMessageChunkDataChildProgressData(UniversalBaseModel):
    child_id: str
    task_label: str
    state: FleetUiMessageChunkDataChildProgressDataState
    elapsed_ms: int
    outcome: typing.Optional[str] = None
    evidence: typing.Optional[typing.List[str]] = None
    gaps: typing.Optional[typing.List[str]] = None
    result_file_count: typing.Optional[int] = None
    code_excerpt: typing.Optional[str] = None
    output_excerpt: typing.Optional[str] = None
    cleanup_state: FleetUiMessageChunkDataChildProgressDataCleanupState
    parent_run_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
