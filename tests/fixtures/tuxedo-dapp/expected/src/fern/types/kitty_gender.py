

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KittyGender(enum.StrEnum):
    MALE = "male"
    FEMALE = "female"

    def visit(self, male: typing.Callable[[], T_Result], female: typing.Callable[[], T_Result]) -> T_Result:
        if self is KittyGender.MALE:
            return male()
        if self is KittyGender.FEMALE:
            return female()
