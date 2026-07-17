

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Gender(enum.StrEnum):
    """
    The gender represents the gender identity of a person.
    """

    MALE = "male"
    FEMALE = "female"
    UNISEX = "unisex"
    OTHER = "other"
    NOT_SPECIFIED = "not_specified"

    def visit(
        self,
        male: typing.Callable[[], T_Result],
        female: typing.Callable[[], T_Result],
        unisex: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        not_specified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Gender.MALE:
            return male()
        if self is Gender.FEMALE:
            return female()
        if self is Gender.UNISEX:
            return unisex()
        if self is Gender.OTHER:
            return other()
        if self is Gender.NOT_SPECIFIED:
            return not_specified()
