

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MutationPatternPayloadRegion(enum.StrEnum):
    CN = "CN"
    US = "US"

    def visit(self, cn: typing.Callable[[], T_Result], us: typing.Callable[[], T_Result]) -> T_Result:
        if self is MutationPatternPayloadRegion.CN:
            return cn()
        if self is MutationPatternPayloadRegion.US:
            return us()
