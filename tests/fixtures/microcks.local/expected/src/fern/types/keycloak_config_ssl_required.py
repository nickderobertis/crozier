

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KeycloakConfigSslRequired(enum.StrEnum):
    """
    SSL certificates requirements
    """

    NONE = "none"
    EXTERNAL = "external"

    def visit(self, none: typing.Callable[[], T_Result], external: typing.Callable[[], T_Result]) -> T_Result:
        if self is KeycloakConfigSslRequired.NONE:
            return none()
        if self is KeycloakConfigSslRequired.EXTERNAL:
            return external()
