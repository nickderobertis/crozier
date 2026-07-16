

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountStatusState(enum.StrEnum):
    """
    The status of the account
    """

    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is AccountStatusState.ENABLED:
            return enabled()
        if self is AccountStatusState.DISABLED:
            return disabled()
