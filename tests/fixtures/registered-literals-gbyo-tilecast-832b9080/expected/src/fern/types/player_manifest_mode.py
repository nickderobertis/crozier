

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayerManifestMode(enum.StrEnum):
    PRESENTATION = "presentation"

    def visit(self, presentation: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlayerManifestMode.PRESENTATION:
            return presentation()
