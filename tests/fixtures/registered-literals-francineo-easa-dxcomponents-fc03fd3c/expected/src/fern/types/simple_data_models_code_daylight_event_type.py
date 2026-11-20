

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsCodeDaylightEventType(enum.StrEnum):
    """
    A time identified in relation with an astronomical event, such as sunrise/sunset,
    represented by a string with an enumerated list of values.
    """

    BMCT = "BMCT"
    SR = "SR"
    SS = "SS"
    EECT = "EECT"

    def visit(
        self,
        bmct: typing.Callable[[], T_Result],
        sr: typing.Callable[[], T_Result],
        ss: typing.Callable[[], T_Result],
        eect: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SimpleDataModelsCodeDaylightEventType.BMCT:
            return bmct()
        if self is SimpleDataModelsCodeDaylightEventType.SR:
            return sr()
        if self is SimpleDataModelsCodeDaylightEventType.SS:
            return ss()
        if self is SimpleDataModelsCodeDaylightEventType.EECT:
            return eect()
