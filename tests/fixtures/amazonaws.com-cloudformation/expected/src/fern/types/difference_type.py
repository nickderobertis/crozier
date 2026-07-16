

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DifferenceType(str, enum.Enum):
    ADD = "ADD"
    REMOVE = "REMOVE"
    NOT_EQUAL = "NOT_EQUAL"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        remove: typing.Callable[[], T_Result],
        not_equal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DifferenceType.ADD:
            return add()
        if self is DifferenceType.REMOVE:
            return remove()
        if self is DifferenceType.NOT_EQUAL:
            return not_equal()
