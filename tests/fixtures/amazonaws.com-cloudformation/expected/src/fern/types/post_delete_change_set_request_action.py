

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDeleteChangeSetRequestAction(enum.StrEnum):
    DELETE_CHANGE_SET = "DeleteChangeSet"

    def visit(self, delete_change_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDeleteChangeSetRequestAction.DELETE_CHANGE_SET:
            return delete_change_set()
