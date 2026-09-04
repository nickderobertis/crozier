

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    WRITE_PETS = "write:pets"
    """
    modify pets in your account
    """

    READ_PETS = "read:pets"
    """
    read your pets
    """

    def visit(self, write_pets: typing.Callable[[], T_Result], read_pets: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.WRITE_PETS:
            return write_pets()
        if self is OauthScope.READ_PETS:
            return read_pets()
