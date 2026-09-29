

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TlsAllowPermissionsItem(enum.StrEnum):
    SELF_SIGNED = "self-signed"

    def visit(self, self_signed: typing.Callable[[], T_Result]) -> T_Result:
        if self is TlsAllowPermissionsItem.SELF_SIGNED:
            return self_signed()
