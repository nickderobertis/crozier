

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WidgetOwner(str, enum.Enum):
    SELF = "self"
    SPOUSE = "spouse"
    CHILD = "child"

    def visit(
        self,
        self_: typing.Callable[[], T_Result],
        spouse: typing.Callable[[], T_Result],
        child: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WidgetOwner.SELF:
            return self_()
        if self is WidgetOwner.SPOUSE:
            return spouse()
        if self is WidgetOwner.CHILD:
            return child()
