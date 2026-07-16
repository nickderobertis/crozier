

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccountFilterType(str, enum.Enum):
    NONE = "NONE"
    INTERSECTION = "INTERSECTION"
    DIFFERENCE = "DIFFERENCE"
    UNION = "UNION"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        intersection: typing.Callable[[], T_Result],
        difference: typing.Callable[[], T_Result],
        union: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountFilterType.NONE:
            return none()
        if self is AccountFilterType.INTERSECTION:
            return intersection()
        if self is AccountFilterType.DIFFERENCE:
            return difference()
        if self is AccountFilterType.UNION:
            return union()
