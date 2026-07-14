

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DagRunRunType(str, enum.Enum):
    BACKFILL = "backfill"
    MANUAL = "manual"
    SCHEDULED = "scheduled"
    DATASET_TRIGGERED = "dataset_triggered"

    def visit(
        self,
        backfill: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        dataset_triggered: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DagRunRunType.BACKFILL:
            return backfill()
        if self is DagRunRunType.MANUAL:
            return manual()
        if self is DagRunRunType.SCHEDULED:
            return scheduled()
        if self is DagRunRunType.DATASET_TRIGGERED:
            return dataset_triggered()
