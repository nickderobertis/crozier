

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaybackDiagnosticsNodesItemRole(enum.StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def visit(self, primary: typing.Callable[[], T_Result], secondary: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlaybackDiagnosticsNodesItemRole.PRIMARY:
            return primary()
        if self is PlaybackDiagnosticsNodesItemRole.SECONDARY:
            return secondary()
