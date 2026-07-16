

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetOperationSummaryAction(enum.StrEnum):
    """
    The type of operation: <code>CREATE</code>, <code>UPDATE</code>, or <code>DELETE</code>. Create and delete operations affect only the specified stack instances that are associated with the specified stack set. Update operations affect both the stack set itself and <i>all</i> associated stack set instances.
    """

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
        if self is StackSetOperationSummaryAction.CREATE:
            return create()
        if self is StackSetOperationSummaryAction.UPDATE:
            return update()
        if self is StackSetOperationSummaryAction.DELETE:
            return delete()
        if self is StackSetOperationSummaryAction.DETECT_DRIFT:
            return detect_drift()
