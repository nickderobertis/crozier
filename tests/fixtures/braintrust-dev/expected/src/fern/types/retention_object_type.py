

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RetentionObjectType(enum.StrEnum):
    """
    The object type that the retention policy applies to
    """

    PROJECT_LOGS = "project_logs"
    EXPERIMENT = "experiment"
    DATASET = "dataset"

    def visit(
        self,
        project_logs: typing.Callable[[], T_Result],
        experiment: typing.Callable[[], T_Result],
        dataset: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RetentionObjectType.PROJECT_LOGS:
            return project_logs()
        if self is RetentionObjectType.EXPERIMENT:
            return experiment()
        if self is RetentionObjectType.DATASET:
            return dataset()
