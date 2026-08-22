

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmailAddress(enum.StrEnum):
    EMAIL = "email"

    def visit(self, email: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmailAddress.EMAIL:
            return email()
