

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAccountRequestType(enum.StrEnum):
    PERSONAL = "personal"
    BUSINESS = "business"
    SOFTWARE = "software"

    def visit(
        self,
        personal: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        software: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateAccountRequestType.PERSONAL:
            return personal()
        if self is CreateAccountRequestType.BUSINESS:
            return business()
        if self is CreateAccountRequestType.SOFTWARE:
            return software()
