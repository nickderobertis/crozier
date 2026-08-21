

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TelephoneNumber(enum.StrEnum):
    TEL = "tel"

    def visit(self, tel: typing.Callable[[], T_Result]) -> T_Result:
        if self is TelephoneNumber.TEL:
            return tel()
