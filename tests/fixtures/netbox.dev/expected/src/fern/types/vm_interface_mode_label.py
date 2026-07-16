

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VmInterfaceModeLabel(str, enum.Enum):
    ACCESS = "Access"
    TAGGED = "Tagged"
    TAGGED_ALL = "Tagged (All)"

    def visit(
        self,
        access: typing.Callable[[], T_Result],
        tagged: typing.Callable[[], T_Result],
        tagged_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VmInterfaceModeLabel.ACCESS:
            return access()
        if self is VmInterfaceModeLabel.TAGGED:
            return tagged()
        if self is VmInterfaceModeLabel.TAGGED_ALL:
            return tagged_all()
