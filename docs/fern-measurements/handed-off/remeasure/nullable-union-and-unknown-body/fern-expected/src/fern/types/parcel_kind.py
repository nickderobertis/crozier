

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParcelKind(enum.StrEnum):
    PARCEL = "parcel"

    def visit(self, parcel: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParcelKind.PARCEL:
            return parcel()
