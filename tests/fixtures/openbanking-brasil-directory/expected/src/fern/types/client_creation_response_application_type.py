

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClientCreationResponseApplicationType(enum.StrEnum):
    """
    OIDC application type response
    """

    WEB = "web"

    def visit(self, web: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClientCreationResponseApplicationType.WEB:
            return web()
