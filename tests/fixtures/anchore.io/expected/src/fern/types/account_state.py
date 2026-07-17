

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountState(enum.StrEnum):
    """
    State of the account. Disabled accounts prevent member users from logging in, deleting accounts are disabled and pending deletion and will be removed once all owned resources are garbage collected by the system
    """

    ENABLED = "enabled"
    DISABLED = "disabled"
    DELETING = "deleting"

    def visit(
        self,
        enabled: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountState.ENABLED:
            return enabled()
        if self is AccountState.DISABLED:
            return disabled()
        if self is AccountState.DELETING:
            return deleting()
