

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ContactGender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    UNISEX = "unisex"

    def visit(
        self,
        male: typing.Callable[[], T_Result],
        female: typing.Callable[[], T_Result],
        unisex: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactGender.MALE:
            return male()
        if self is ContactGender.FEMALE:
            return female()
        if self is ContactGender.UNISEX:
            return unisex()
