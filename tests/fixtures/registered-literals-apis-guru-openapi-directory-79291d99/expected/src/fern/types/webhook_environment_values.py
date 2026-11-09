

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookEnvironmentValues(enum.StrEnum):
    """
    The Plaid environment the webhook was sent from
    """

    DEVELOPMENT = "development"
    SANDBOX = "sandbox"
    PRODUCTION = "production"

    def visit(
        self,
        development: typing.Callable[[], T_Result],
        sandbox: typing.Callable[[], T_Result],
        production: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookEnvironmentValues.DEVELOPMENT:
            return development()
        if self is WebhookEnvironmentValues.SANDBOX:
            return sandbox()
        if self is WebhookEnvironmentValues.PRODUCTION:
            return production()
