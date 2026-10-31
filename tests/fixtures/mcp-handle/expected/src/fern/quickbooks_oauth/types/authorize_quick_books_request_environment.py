

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizeQuickBooksRequestEnvironment(enum.StrEnum):
    """
    QuickBooks environment to authorize ('sandbox' or 'production')
    """

    SANDBOX = "sandbox"
    PRODUCTION = "production"

    def visit(self, sandbox: typing.Callable[[], T_Result], production: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthorizeQuickBooksRequestEnvironment.SANDBOX:
            return sandbox()
        if self is AuthorizeQuickBooksRequestEnvironment.PRODUCTION:
            return production()
