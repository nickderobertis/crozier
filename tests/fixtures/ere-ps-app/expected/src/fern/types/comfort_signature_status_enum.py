

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ComfortSignatureStatusEnum(enum.StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is ComfortSignatureStatusEnum.ENABLED:
            return enabled()
        if self is ComfortSignatureStatusEnum.DISABLED:
            return disabled()
