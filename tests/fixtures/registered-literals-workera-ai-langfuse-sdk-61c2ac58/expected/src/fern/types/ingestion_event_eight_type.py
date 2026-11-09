

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventEightType(enum.StrEnum):
    OBSERVATION_CREATE = "observation-create"

    def visit(self, observation_create: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventEightType.OBSERVATION_CREATE:
            return observation_create()
