

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LampGadgetKind(enum.StrEnum):
    LAMP = "LAMP"

    def visit(self, lamp: typing.Callable[[], T_Result]) -> T_Result:
        if self is LampGadgetKind.LAMP:
            return lamp()
