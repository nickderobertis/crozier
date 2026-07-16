

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfaceModeLabel(str, enum.Enum):
    ACCESS = "Access"
    TAGGED = "Tagged"
    TAGGED_ALL = "Tagged (All)"

    def visit(
        self,
        access: typing.Callable[[], T_Result],
        tagged: typing.Callable[[], T_Result],
        tagged_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfaceModeLabel.ACCESS:
            return access()
        if self is InterfaceModeLabel.TAGGED:
            return tagged()
        if self is InterfaceModeLabel.TAGGED_ALL:
            return tagged_all()
