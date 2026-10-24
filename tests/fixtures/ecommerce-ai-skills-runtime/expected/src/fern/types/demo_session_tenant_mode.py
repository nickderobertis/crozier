

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DemoSessionTenantMode(enum.StrEnum):
    DEMO = "demo"

    def visit(self, demo: typing.Callable[[], T_Result]) -> T_Result:
        if self is DemoSessionTenantMode.DEMO:
            return demo()
