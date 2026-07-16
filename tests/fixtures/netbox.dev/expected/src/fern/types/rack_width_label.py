

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RackWidthLabel(str, enum.Enum):
    TEN_INCHES = "10 inches"
    NINETEEN_INCHES = "19 inches"
    TWENTY_ONE_INCHES = "21 inches"
    TWENTY_THREE_INCHES = "23 inches"

    def visit(
        self,
        ten_inches: typing.Callable[[], T_Result],
        nineteen_inches: typing.Callable[[], T_Result],
        twenty_one_inches: typing.Callable[[], T_Result],
        twenty_three_inches: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RackWidthLabel.TEN_INCHES:
            return ten_inches()
        if self is RackWidthLabel.NINETEEN_INCHES:
            return nineteen_inches()
        if self is RackWidthLabel.TWENTY_ONE_INCHES:
            return twenty_one_inches()
        if self is RackWidthLabel.TWENTY_THREE_INCHES:
            return twenty_three_inches()
