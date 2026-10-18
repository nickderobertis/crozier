

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModesZero(enum.StrEnum):
    LIFECYCLE = "lifecycle"
    RUN_MODES = "run_modes"
    STATE_UPDATE = "state_update"

    def visit(
        self,
        lifecycle: typing.Callable[[], T_Result],
        run_modes: typing.Callable[[], T_Result],
        state_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModesZero.LIFECYCLE:
            return lifecycle()
        if self is JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModesZero.RUN_MODES:
            return run_modes()
        if self is JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModesZero.STATE_UPDATE:
            return state_update()
