

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetCreateChangeSetRequestAction(str, enum.Enum):
    CREATE_CHANGE_SET = "CreateChangeSet"

    def visit(self, create_change_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCreateChangeSetRequestAction.CREATE_CHANGE_SET:
            return create_change_set()
