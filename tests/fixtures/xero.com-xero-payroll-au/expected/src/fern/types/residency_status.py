

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResidencyStatus(str, enum.Enum):
    AUSTRALIANRESIDENT = "AUSTRALIANRESIDENT"
    FOREIGNRESIDENT = "FOREIGNRESIDENT"
    WORKINGHOLIDAYMAKER = "WORKINGHOLIDAYMAKER"

    def visit(
        self,
        australianresident: typing.Callable[[], T_Result],
        foreignresident: typing.Callable[[], T_Result],
        workingholidaymaker: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResidencyStatus.AUSTRALIANRESIDENT:
            return australianresident()
        if self is ResidencyStatus.FOREIGNRESIDENT:
            return foreignresident()
        if self is ResidencyStatus.WORKINGHOLIDAYMAKER:
            return workingholidaymaker()
