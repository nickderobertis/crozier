

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WidgetStatus(str, enum.Enum):
    ZERO_ACTIVE = "0: Active"
    ONE_IN_ACTIVE = "1: InActive"

    def visit(
        self, zero_active: typing.Callable[[], T_Result], one_in_active: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WidgetStatus.ZERO_ACTIVE:
            return zero_active()
        if self is WidgetStatus.ONE_IN_ACTIVE:
            return one_in_active()
