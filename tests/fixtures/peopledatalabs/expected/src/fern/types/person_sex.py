

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PersonSex(enum.StrEnum):
    """
    The person's sex
    """

    MALE = "male"
    FEMALE = "female"

    def visit(self, male: typing.Callable[[], T_Result], female: typing.Callable[[], T_Result]) -> T_Result:
        if self is PersonSex.MALE:
            return male()
        if self is PersonSex.FEMALE:
            return female()
