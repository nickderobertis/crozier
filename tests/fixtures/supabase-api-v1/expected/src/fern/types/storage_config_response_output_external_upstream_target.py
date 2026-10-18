

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageConfigResponseOutputExternalUpstreamTarget(enum.StrEnum):
    MAIN = "main"
    CANARY = "canary"

    def visit(self, main: typing.Callable[[], T_Result], canary: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageConfigResponseOutputExternalUpstreamTarget.MAIN:
            return main()
        if self is StorageConfigResponseOutputExternalUpstreamTarget.CANARY:
            return canary()
