

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateStorageConfigBodyExternalUpstreamTarget(enum.StrEnum):
    MAIN = "main"
    CANARY = "canary"

    def visit(self, main: typing.Callable[[], T_Result], canary: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateStorageConfigBodyExternalUpstreamTarget.MAIN:
            return main()
        if self is UpdateStorageConfigBodyExternalUpstreamTarget.CANARY:
            return canary()
