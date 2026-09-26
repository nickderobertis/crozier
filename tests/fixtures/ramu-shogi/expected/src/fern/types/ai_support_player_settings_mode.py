

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AiSupportPlayerSettingsMode(enum.StrEnum):
    UNLIMITED = "unlimited"
    LIMITED = "limited"

    def visit(self, unlimited: typing.Callable[[], T_Result], limited: typing.Callable[[], T_Result]) -> T_Result:
        if self is AiSupportPlayerSettingsMode.UNLIMITED:
            return unlimited()
        if self is AiSupportPlayerSettingsMode.LIMITED:
            return limited()
