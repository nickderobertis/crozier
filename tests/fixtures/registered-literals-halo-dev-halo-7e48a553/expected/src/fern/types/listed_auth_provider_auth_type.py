

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListedAuthProviderAuthType(enum.StrEnum):
    FORM = "FORM"
    OAUTH2 = "OAUTH2"

    def visit(self, form: typing.Callable[[], T_Result], oauth2: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListedAuthProviderAuthType.FORM:
            return form()
        if self is ListedAuthProviderAuthType.OAUTH2:
            return oauth2()
