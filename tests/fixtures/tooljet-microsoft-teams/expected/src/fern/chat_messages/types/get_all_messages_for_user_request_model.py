

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAllMessagesForUserRequestModel(enum.StrEnum):
    A = "A"
    B = "B"

    def visit(self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAllMessagesForUserRequestModel.A:
            return a()
        if self is GetAllMessagesForUserRequestModel.B:
            return b()
