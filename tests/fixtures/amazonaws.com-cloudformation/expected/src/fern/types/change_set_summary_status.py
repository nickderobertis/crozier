

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeSetSummaryStatus(enum.StrEnum):
    """
    The state of the change set, such as <code>CREATE_IN_PROGRESS</code>, <code>CREATE_COMPLETE</code>, or <code>FAILED</code>.
    """

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_PENDING = "DELETE_PENDING"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"
    FAILED = "FAILED"

    def visit(
        self,
        create_pending: typing.Callable[[], T_Result],
        create_in_progress: typing.Callable[[], T_Result],
        create_complete: typing.Callable[[], T_Result],
        delete_pending: typing.Callable[[], T_Result],
        delete_in_progress: typing.Callable[[], T_Result],
        delete_complete: typing.Callable[[], T_Result],
        delete_failed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChangeSetSummaryStatus.CREATE_PENDING:
            return create_pending()
        if self is ChangeSetSummaryStatus.CREATE_IN_PROGRESS:
            return create_in_progress()
        if self is ChangeSetSummaryStatus.CREATE_COMPLETE:
            return create_complete()
        if self is ChangeSetSummaryStatus.DELETE_PENDING:
            return delete_pending()
        if self is ChangeSetSummaryStatus.DELETE_IN_PROGRESS:
            return delete_in_progress()
        if self is ChangeSetSummaryStatus.DELETE_COMPLETE:
            return delete_complete()
        if self is ChangeSetSummaryStatus.DELETE_FAILED:
            return delete_failed()
        if self is ChangeSetSummaryStatus.FAILED:
            return failed()
