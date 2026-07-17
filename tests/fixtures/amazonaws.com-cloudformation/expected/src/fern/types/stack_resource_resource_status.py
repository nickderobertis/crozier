

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackResourceResourceStatus(enum.StrEnum):
    """
    Current status of the resource.
    """

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_SKIPPED = "DELETE_SKIPPED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    IMPORT_FAILED = "IMPORT_FAILED"
    IMPORT_COMPLETE = "IMPORT_COMPLETE"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"
    IMPORT_ROLLBACK_IN_PROGRESS = "IMPORT_ROLLBACK_IN_PROGRESS"
    IMPORT_ROLLBACK_FAILED = "IMPORT_ROLLBACK_FAILED"
    IMPORT_ROLLBACK_COMPLETE = "IMPORT_ROLLBACK_COMPLETE"
    UPDATE_ROLLBACK_IN_PROGRESS = "UPDATE_ROLLBACK_IN_PROGRESS"
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"

    def visit(
        self,
        create_in_progress: typing.Callable[[], T_Result],
        create_failed: typing.Callable[[], T_Result],
        create_complete: typing.Callable[[], T_Result],
        delete_in_progress: typing.Callable[[], T_Result],
        delete_failed: typing.Callable[[], T_Result],
        delete_complete: typing.Callable[[], T_Result],
        delete_skipped: typing.Callable[[], T_Result],
        update_in_progress: typing.Callable[[], T_Result],
        update_failed: typing.Callable[[], T_Result],
        update_complete: typing.Callable[[], T_Result],
        import_failed: typing.Callable[[], T_Result],
        import_complete: typing.Callable[[], T_Result],
        import_in_progress: typing.Callable[[], T_Result],
        import_rollback_in_progress: typing.Callable[[], T_Result],
        import_rollback_failed: typing.Callable[[], T_Result],
        import_rollback_complete: typing.Callable[[], T_Result],
        update_rollback_in_progress: typing.Callable[[], T_Result],
        update_rollback_complete: typing.Callable[[], T_Result],
        update_rollback_failed: typing.Callable[[], T_Result],
        rollback_in_progress: typing.Callable[[], T_Result],
        rollback_complete: typing.Callable[[], T_Result],
        rollback_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackResourceResourceStatus.CREATE_IN_PROGRESS:
            return create_in_progress()
        if self is StackResourceResourceStatus.CREATE_FAILED:
            return create_failed()
        if self is StackResourceResourceStatus.CREATE_COMPLETE:
            return create_complete()
        if self is StackResourceResourceStatus.DELETE_IN_PROGRESS:
            return delete_in_progress()
        if self is StackResourceResourceStatus.DELETE_FAILED:
            return delete_failed()
        if self is StackResourceResourceStatus.DELETE_COMPLETE:
            return delete_complete()
        if self is StackResourceResourceStatus.DELETE_SKIPPED:
            return delete_skipped()
        if self is StackResourceResourceStatus.UPDATE_IN_PROGRESS:
            return update_in_progress()
        if self is StackResourceResourceStatus.UPDATE_FAILED:
            return update_failed()
        if self is StackResourceResourceStatus.UPDATE_COMPLETE:
            return update_complete()
        if self is StackResourceResourceStatus.IMPORT_FAILED:
            return import_failed()
        if self is StackResourceResourceStatus.IMPORT_COMPLETE:
            return import_complete()
        if self is StackResourceResourceStatus.IMPORT_IN_PROGRESS:
            return import_in_progress()
        if self is StackResourceResourceStatus.IMPORT_ROLLBACK_IN_PROGRESS:
            return import_rollback_in_progress()
        if self is StackResourceResourceStatus.IMPORT_ROLLBACK_FAILED:
            return import_rollback_failed()
        if self is StackResourceResourceStatus.IMPORT_ROLLBACK_COMPLETE:
            return import_rollback_complete()
        if self is StackResourceResourceStatus.UPDATE_ROLLBACK_IN_PROGRESS:
            return update_rollback_in_progress()
        if self is StackResourceResourceStatus.UPDATE_ROLLBACK_COMPLETE:
            return update_rollback_complete()
        if self is StackResourceResourceStatus.UPDATE_ROLLBACK_FAILED:
            return update_rollback_failed()
        if self is StackResourceResourceStatus.ROLLBACK_IN_PROGRESS:
            return rollback_in_progress()
        if self is StackResourceResourceStatus.ROLLBACK_COMPLETE:
            return rollback_complete()
        if self is StackResourceResourceStatus.ROLLBACK_FAILED:
            return rollback_failed()
