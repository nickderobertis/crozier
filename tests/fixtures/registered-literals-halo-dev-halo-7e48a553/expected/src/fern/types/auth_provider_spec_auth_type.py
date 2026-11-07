

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthProviderSpecAuthType(enum.StrEnum):
    """
    Auth type: form or oauth2.
    """

    FORM = "FORM"
    OAUTH2 = "OAUTH2"

    def visit(self, form: typing.Callable[[], T_Result], oauth2: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthProviderSpecAuthType.FORM:
            return form()
        if self is AuthProviderSpecAuthType.OAUTH2:
            return oauth2()
