

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetExecuteChangeSetRequestAction(str, enum.Enum):
    EXECUTE_CHANGE_SET = "ExecuteChangeSet"

    def visit(self, execute_change_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetExecuteChangeSetRequestAction.EXECUTE_CHANGE_SET:
            return execute_change_set()
