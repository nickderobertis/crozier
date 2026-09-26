

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConflictErrorBodyCode(enum.StrEnum):
    SNAPSHOT_JOB_STATE_CONFLICT = "SNAPSHOT_JOB_STATE_CONFLICT"
    SNAPSHOT_JOB_OWNERSHIP_MISMATCH = "SNAPSHOT_JOB_OWNERSHIP_MISMATCH"

    def visit(
        self,
        snapshot_job_state_conflict: typing.Callable[[], T_Result],
        snapshot_job_ownership_mismatch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConflictErrorBodyCode.SNAPSHOT_JOB_STATE_CONFLICT:
            return snapshot_job_state_conflict()
        if self is ConflictErrorBodyCode.SNAPSHOT_JOB_OWNERSHIP_MISMATCH:
            return snapshot_job_ownership_mismatch()
