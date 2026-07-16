

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDeleteChangeSetRequestAction(str, enum.Enum):
    DELETE_CHANGE_SET = "DeleteChangeSet"

    def visit(self, delete_change_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeleteChangeSetRequestAction.DELETE_CHANGE_SET:
            return delete_change_set()
