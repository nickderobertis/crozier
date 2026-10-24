

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PrincipalTenantMode(enum.StrEnum):
    PRODUCTION = "production"
    DEMO = "demo"

    def visit(self, production: typing.Callable[[], T_Result], demo: typing.Callable[[], T_Result]) -> T_Result:
        if self is PrincipalTenantMode.PRODUCTION:
            return production()
        if self is PrincipalTenantMode.DEMO:
            return demo()
