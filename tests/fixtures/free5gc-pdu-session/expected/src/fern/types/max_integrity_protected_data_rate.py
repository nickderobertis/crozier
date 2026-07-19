

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MaxIntegrityProtectedDataRate(enum.StrEnum):
    SIXTY_FOUR_KBPS = "64_KBPS"
    MAX_UE_RATE = "MAX_UE_RATE"

    def visit(
        self, sixty_four_kbps: typing.Callable[[], T_Result], max_ue_rate: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is MaxIntegrityProtectedDataRate.SIXTY_FOUR_KBPS:
            return sixty_four_kbps()
        if self is MaxIntegrityProtectedDataRate.MAX_UE_RATE:
            return max_ue_rate()
