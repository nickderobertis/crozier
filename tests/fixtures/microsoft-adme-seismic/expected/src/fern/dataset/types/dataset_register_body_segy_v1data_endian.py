

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetRegisterBodySegyV1DataEndian(enum.StrEnum):
    """
    Endianness of binary value.  Enumeration: "BIG", "LITTLE".  If absent, applications will need to interpret from context indicators.
    """

    BIG = "BIG"
    LITTLE = "LITTLE"

    def visit(self, big: typing.Callable[[], T_Result], little: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetRegisterBodySegyV1DataEndian.BIG:
            return big()
        if self is DatasetRegisterBodySegyV1DataEndian.LITTLE:
            return little()
