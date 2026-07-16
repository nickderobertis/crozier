

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableInterfaceDuplex(str, enum.Enum):
    HALF = "half"
    FULL = "full"
    AUTO = "auto"

    def visit(
        self,
        half: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableInterfaceDuplex.HALF:
            return half()
        if self is WritableInterfaceDuplex.FULL:
            return full()
        if self is WritableInterfaceDuplex.AUTO:
            return auto()
