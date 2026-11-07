

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderType(enum.StrEnum):
    MANAGED = "managed"
    UNMANAGED = "unmanaged"

    def visit(self, managed: typing.Callable[[], T_Result], unmanaged: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProviderType.MANAGED:
            return managed()
        if self is ProviderType.UNMANAGED:
            return unmanaged()
