

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WidgetScope(str, enum.Enum):
    GLOBAL = "global"
    PRACTICE = "practice"
    INTENT = "intent"

    def visit(
        self,
        global_: typing.Callable[[], T_Result],
        practice: typing.Callable[[], T_Result],
        intent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WidgetScope.GLOBAL:
            return global_()
        if self is WidgetScope.PRACTICE:
            return practice()
        if self is WidgetScope.INTENT:
            return intent()
