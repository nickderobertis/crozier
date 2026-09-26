

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InputDatePayloadFormat(enum.StrEnum):
    """
    Display format for the date.
    """

    MM_DD_YYYY = "MM/dd/yyyy"
    DD_MM_YYYY = "dd/MM/yyyy"
    YYYY_MM_DD = "yyyy/MM/dd"

    def visit(
        self,
        mm_dd_yyyy: typing.Callable[[], T_Result],
        dd_mm_yyyy: typing.Callable[[], T_Result],
        yyyy_mm_dd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InputDatePayloadFormat.MM_DD_YYYY:
            return mm_dd_yyyy()
        if self is InputDatePayloadFormat.DD_MM_YYYY:
            return dd_mm_yyyy()
        if self is InputDatePayloadFormat.YYYY_MM_DD:
            return yyyy_mm_dd()
