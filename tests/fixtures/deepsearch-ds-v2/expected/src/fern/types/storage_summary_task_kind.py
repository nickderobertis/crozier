

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageSummaryTaskKind(enum.StrEnum):
    PROJECT_TASK = "project_task"
    CELERY_TASK = "celery_task"

    def visit(
        self, project_task: typing.Callable[[], T_Result], celery_task: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is StorageSummaryTaskKind.PROJECT_TASK:
            return project_task()
        if self is StorageSummaryTaskKind.CELERY_TASK:
            return celery_task()
