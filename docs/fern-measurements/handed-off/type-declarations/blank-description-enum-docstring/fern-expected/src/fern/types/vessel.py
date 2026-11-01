

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Vessel(enum.StrEnum):
    """ """

    CATAMARAN = "CATAMARAN"
    MONOHULL = "MONOHULL"

    def visit(self, catamaran: typing.Callable[[], T_Result], monohull: typing.Callable[[], T_Result]) -> T_Result:
        if self is Vessel.CATAMARAN:
            return catamaran()
        if self is Vessel.MONOHULL:
            return monohull()
