

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UsageState(str, enum.Enum):
    """
    Usage state of the onboarded instance of the application package
    """

    IN_USE = "IN_USE"
    NOT_IN_USE = "NOT_IN_USE"

    def visit(self, in_use: typing.Callable[[], T_Result], not_in_use: typing.Callable[[], T_Result]) -> T_Result:
        if self is UsageState.IN_USE:
            return in_use()
        if self is UsageState.NOT_IN_USE:
            return not_in_use()
