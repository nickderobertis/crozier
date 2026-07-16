

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VmInterfaceModeValue(enum.StrEnum):
    ACCESS = "access"
    TAGGED = "tagged"
    TAGGED_ALL = "tagged-all"

    def visit(
        self,
        access: typing.Callable[[], T_Result],
        tagged: typing.Callable[[], T_Result],
        tagged_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VmInterfaceModeValue.ACCESS:
            return access()
        if self is VmInterfaceModeValue.TAGGED:
            return tagged()
        if self is VmInterfaceModeValue.TAGGED_ALL:
            return tagged_all()
