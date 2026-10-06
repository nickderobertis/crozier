

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordingSnapshotState(enum.StrEnum):
    WAITING_FOR_AUDIO = "waiting-for-audio"
    RECORDING = "recording"
    FINALIZING = "finalizing"
    COMPLETE = "complete"
    INTERRUPTED = "interrupted"
    EMPTY = "empty"

    def visit(
        self,
        waiting_for_audio: typing.Callable[[], T_Result],
        recording: typing.Callable[[], T_Result],
        finalizing: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        interrupted: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RecordingSnapshotState.WAITING_FOR_AUDIO:
            return waiting_for_audio()
        if self is RecordingSnapshotState.RECORDING:
            return recording()
        if self is RecordingSnapshotState.FINALIZING:
            return finalizing()
        if self is RecordingSnapshotState.COMPLETE:
            return complete()
        if self is RecordingSnapshotState.INTERRUPTED:
            return interrupted()
        if self is RecordingSnapshotState.EMPTY:
            return empty()
