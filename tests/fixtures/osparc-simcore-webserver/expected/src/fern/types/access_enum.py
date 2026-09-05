

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessEnum(enum.StrEnum):
    READ_AND_WRITE = "ReadAndWrite"
    INVISIBLE = "Invisible"
    READ_ONLY = "ReadOnly"

    def visit(
        self,
        read_and_write: typing.Callable[[], T_Result],
        invisible: typing.Callable[[], T_Result],
        read_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccessEnum.READ_AND_WRITE:
            return read_and_write()
        if self is AccessEnum.INVISIBLE:
            return invisible()
        if self is AccessEnum.READ_ONLY:
            return read_only()
