

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetPatchOpenzgyV1DataEndian(enum.StrEnum):
    """
    Endianness of binary value.  Enumeration: "BIG", "LITTLE".  If absent, applications will need to interpret from context indicators.
    """

    BIG = "BIG"
    LITTLE = "LITTLE"

    def visit(self, big: typing.Callable[[], T_Result], little: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetPatchOpenzgyV1DataEndian.BIG:
            return big()
        if self is DatasetPatchOpenzgyV1DataEndian.LITTLE:
            return little()
