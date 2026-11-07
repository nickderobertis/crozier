

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AuditLogFetchByCursorResponseItemsItemRelatedType(enum.StrEnum):
    MONITOR = "Monitor"
    NOTIFICATION = "Notification"
    TASK = "Task"
    FUNCTION_WORKER = "FunctionWorker"

    def visit(
        self,
        monitor: typing.Callable[[], T_Result],
        notification: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        function_worker: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuditLogFetchByCursorResponseItemsItemRelatedType.MONITOR:
            return monitor()
        if self is AuditLogFetchByCursorResponseItemsItemRelatedType.NOTIFICATION:
            return notification()
        if self is AuditLogFetchByCursorResponseItemsItemRelatedType.TASK:
            return task()
        if self is AuditLogFetchByCursorResponseItemsItemRelatedType.FUNCTION_WORKER:
            return function_worker()
