

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetOperationAction(enum.StrEnum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    DETECT_DRIFT = "DETECT_DRIFT"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        detect_drift: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackSetOperationAction.CREATE:
            return create()
        if self is StackSetOperationAction.UPDATE:
            return update()
        if self is StackSetOperationAction.DELETE:
            return delete()
        if self is StackSetOperationAction.DETECT_DRIFT:
            return detect_drift()
