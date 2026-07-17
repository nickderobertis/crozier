

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntegrationState(enum.StrEnum):
    """
    The current state of the Integration.
    """

    DISABLED = "disabled"
    NEEDS_CONFIGURATION = "needs_configuration"
    CONFIGURED = "configured"

    def visit(
        self,
        disabled: typing.Callable[[], T_Result],
        needs_configuration: typing.Callable[[], T_Result],
        configured: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IntegrationState.DISABLED:
            return disabled()
        if self is IntegrationState.NEEDS_CONFIGURATION:
            return needs_configuration()
        if self is IntegrationState.CONFIGURED:
            return configured()
