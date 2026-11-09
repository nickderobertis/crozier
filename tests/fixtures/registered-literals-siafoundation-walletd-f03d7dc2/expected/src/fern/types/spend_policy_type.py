

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpendPolicyType(enum.StrEnum):
    """
    Policy discriminator.
    """

    ABOVE = "above"
    AFTER = "after"
    PK = "pk"
    H = "h"
    THRESH = "thresh"
    OPAQUE = "opaque"
    UC = "uc"

    def visit(
        self,
        above: typing.Callable[[], T_Result],
        after: typing.Callable[[], T_Result],
        pk: typing.Callable[[], T_Result],
        h: typing.Callable[[], T_Result],
        thresh: typing.Callable[[], T_Result],
        opaque: typing.Callable[[], T_Result],
        uc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SpendPolicyType.ABOVE:
            return above()
        if self is SpendPolicyType.AFTER:
            return after()
        if self is SpendPolicyType.PK:
            return pk()
        if self is SpendPolicyType.H:
            return h()
        if self is SpendPolicyType.THRESH:
            return thresh()
        if self is SpendPolicyType.OPAQUE:
            return opaque()
        if self is SpendPolicyType.UC:
            return uc()
