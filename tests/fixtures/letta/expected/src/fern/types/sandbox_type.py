

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxType(enum.StrEnum):
    E2B = "e2b"
    MODAL = "modal"
    LOCAL = "local"

    def visit(
        self,
        e2b: typing.Callable[[], T_Result],
        modal: typing.Callable[[], T_Result],
        local: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SandboxType.E2B:
            return e2b()
        if self is SandboxType.MODAL:
            return modal()
        if self is SandboxType.LOCAL:
            return local()
