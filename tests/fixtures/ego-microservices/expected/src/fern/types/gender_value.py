

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenderValue(enum.StrEnum):
    """
    An enumeration.
    """

    MALE = "male"
    FEMALE = "female"

    def visit(self, male: typing.Callable[[], T_Result], female: typing.Callable[[], T_Result]) -> T_Result:
        if self is GenderValue.MALE:
            return male()
        if self is GenderValue.FEMALE:
            return female()
