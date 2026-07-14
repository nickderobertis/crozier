

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UpdateTopicStatusRequestEnabled(str, enum.Enum):
    TRUE = "true"
    FALSE = "false"

    def visit(self, true: typing.Callable[[], T_Result], false: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateTopicStatusRequestEnabled.TRUE:
            return true()
        if self is UpdateTopicStatusRequestEnabled.FALSE:
            return false()
