

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObExternalDirectDebitStatus1Code(enum.StrEnum):
    """
    Specifies the status of the direct debit in code form.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObExternalDirectDebitStatus1Code.ACTIVE:
            return active()
        if self is ObExternalDirectDebitStatus1Code.INACTIVE:
            return inactive()
