

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AllowanceType(str, enum.Enum):
    CAR = "CAR"
    TRANSPORT = "TRANSPORT"
    TRAVEL = "TRAVEL"
    LAUNDRY = "LAUNDRY"
    MEALS = "MEALS"
    JOBKEEPER = "JOBKEEPER"
    OTHER = "OTHER"

    def visit(
        self,
        car: typing.Callable[[], T_Result],
        transport: typing.Callable[[], T_Result],
        travel: typing.Callable[[], T_Result],
        laundry: typing.Callable[[], T_Result],
        meals: typing.Callable[[], T_Result],
        jobkeeper: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowanceType.CAR:
            return car()
        if self is AllowanceType.TRANSPORT:
            return transport()
        if self is AllowanceType.TRAVEL:
            return travel()
        if self is AllowanceType.LAUNDRY:
            return laundry()
        if self is AllowanceType.MEALS:
            return meals()
        if self is AllowanceType.JOBKEEPER:
            return jobkeeper()
        if self is AllowanceType.OTHER:
            return other()
