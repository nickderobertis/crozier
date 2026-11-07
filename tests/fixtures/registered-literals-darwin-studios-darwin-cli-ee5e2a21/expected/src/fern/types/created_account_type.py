

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreatedAccountType(enum.StrEnum):
    PERSONAL = "personal"
    BUSINESS = "business"
    SOFTWARE = "software"

    def visit(
        self,
        personal: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        software: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreatedAccountType.PERSONAL:
            return personal()
        if self is CreatedAccountType.BUSINESS:
            return business()
        if self is CreatedAccountType.SOFTWARE:
            return software()
