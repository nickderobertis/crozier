

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VectorStoreItemModelIdOne(enum.StrEnum):
    PLATFORM = "platform"

    def visit(self, platform: typing.Callable[[], T_Result]) -> T_Result:
        if self is VectorStoreItemModelIdOne.PLATFORM:
            return platform()
