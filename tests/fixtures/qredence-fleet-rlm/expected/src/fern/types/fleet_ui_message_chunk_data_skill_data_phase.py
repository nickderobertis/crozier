

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FleetUiMessageChunkDataSkillDataPhase(enum.StrEnum):
    ACTIVATED = "activated"
    LOADED = "loaded"

    def visit(self, activated: typing.Callable[[], T_Result], loaded: typing.Callable[[], T_Result]) -> T_Result:
        if self is FleetUiMessageChunkDataSkillDataPhase.ACTIVATED:
            return activated()
        if self is FleetUiMessageChunkDataSkillDataPhase.LOADED:
            return loaded()
