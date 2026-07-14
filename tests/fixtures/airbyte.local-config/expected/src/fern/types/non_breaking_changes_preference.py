

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NonBreakingChangesPreference(str, enum.Enum):
    IGNORE = "ignore"
    DISABLE = "disable"

    def visit(self, ignore: typing.Callable[[], T_Result], disable: typing.Callable[[], T_Result]) -> T_Result:
        if self is NonBreakingChangesPreference.IGNORE:
            return ignore()
        if self is NonBreakingChangesPreference.DISABLE:
            return disable()
