

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfaceDuplexLabel(str, enum.Enum):
    HALF = "Half"
    FULL = "Full"
    AUTO = "Auto"

    def visit(
        self,
        half: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfaceDuplexLabel.HALF:
            return half()
        if self is InterfaceDuplexLabel.FULL:
            return full()
        if self is InterfaceDuplexLabel.AUTO:
            return auto()
