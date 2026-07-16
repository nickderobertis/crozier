

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableVmInterfaceMode(str, enum.Enum):
    ACCESS = "access"
    TAGGED = "tagged"
    TAGGED_ALL = "tagged-all"

    def visit(
        self,
        access: typing.Callable[[], T_Result],
        tagged: typing.Callable[[], T_Result],
        tagged_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableVmInterfaceMode.ACCESS:
            return access()
        if self is WritableVmInterfaceMode.TAGGED:
            return tagged()
        if self is WritableVmInterfaceMode.TAGGED_ALL:
            return tagged_all()
