

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeleteImageResponseStatus(str, enum.Enum):
    """
    Current status of the image deletion
    """

    NOT_FOUND = "not_found"
    DELETING = "deleting"
    DELETE_FAILED = "delete_failed"

    def visit(
        self,
        not_found: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
        delete_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeleteImageResponseStatus.NOT_FOUND:
            return not_found()
        if self is DeleteImageResponseStatus.DELETING:
            return deleting()
        if self is DeleteImageResponseStatus.DELETE_FAILED:
            return delete_failed()
