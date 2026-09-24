

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SerialConfigParity(enum.StrEnum):
    """
    The parity for the serial connection
    """

    NONE = "NONE"
    EVEN = "EVEN"
    ODD = "ODD"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        even: typing.Callable[[], T_Result],
        odd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SerialConfigParity.NONE:
            return none()
        if self is SerialConfigParity.EVEN:
            return even()
        if self is SerialConfigParity.ODD:
            return odd()
