

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WidgetBinding(str, enum.Enum):
    CLS = "cls"
    INSTANCE = "instance"
    STATIC = "static"

    def visit(
        self,
        cls: typing.Callable[[], T_Result],
        instance: typing.Callable[[], T_Result],
        static: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WidgetBinding.CLS:
            return cls()
        if self is WidgetBinding.INSTANCE:
            return instance()
        if self is WidgetBinding.STATIC:
            return static()
