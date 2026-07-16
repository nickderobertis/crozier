

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfaceModeValue(str, enum.Enum):
    ACCESS = "access"
    TAGGED = "tagged"
    TAGGED_ALL = "tagged-all"

    def visit(
        self,
        access: typing.Callable[[], T_Result],
        tagged: typing.Callable[[], T_Result],
        tagged_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfaceModeValue.ACCESS:
            return access()
        if self is InterfaceModeValue.TAGGED:
            return tagged()
        if self is InterfaceModeValue.TAGGED_ALL:
            return tagged_all()
