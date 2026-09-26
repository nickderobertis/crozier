

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteReplyEntityNameOne(enum.StrEnum):
    CUSTOMER = "customer"

    def visit(self, customer: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteReplyEntityNameOne.CUSTOMER:
            return customer()
