

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recording_snapshot_source import RecordingSnapshotSource
from .recording_snapshot_state import RecordingSnapshotState


class RecordingSnapshot(UniversalBaseModel):
    audio_started_at: typing.Optional[str] = None
    bytes: int
    created_at: str
    duplicate_packets: int
    duration_seconds: float
    error: typing.Optional[str] = None
    file_name: typing.Optional[str] = None
    finished_at: typing.Optional[str] = None
    frames: int
    gap_packets: int
    id: str
    source: RecordingSnapshotSource
    state: RecordingSnapshotState
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
