

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostCreateChangeSetRequestAction(str, enum.Enum):
    CREATE_CHANGE_SET = "CreateChangeSet"

    def visit(self, create_change_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostCreateChangeSetRequestAction.CREATE_CHANGE_SET:
            return create_change_set()
