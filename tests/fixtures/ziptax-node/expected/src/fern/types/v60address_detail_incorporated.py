

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V60AddressDetailIncorporated(enum.StrEnum):
    """
    Whether the location falls within incorporated city limits, as the string 'true' or 'false'.
    """

    TRUE = "true"
    FALSE = "false"

    def visit(self, true: typing.Callable[[], T_Result], false: typing.Callable[[], T_Result]) -> T_Result:
        if self is V60AddressDetailIncorporated.TRUE:
            return true()
        if self is V60AddressDetailIncorporated.FALSE:
            return false()
