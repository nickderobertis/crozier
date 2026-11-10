

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventNineType(enum.StrEnum):
    OBSERVATION_UPDATE = "observation-update"

    def visit(self, observation_update: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventNineType.OBSERVATION_UPDATE:
            return observation_update()
