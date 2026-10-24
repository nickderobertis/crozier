

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarketplaceAccountCredentialRefsValue(enum.StrEnum):
    PRESENT = "present"

    def visit(self, present: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarketplaceAccountCredentialRefsValue.PRESENT:
            return present()
