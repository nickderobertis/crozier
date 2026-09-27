

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLeadsV3RequestView(enum.StrEnum):
    STAGES = "stages"

    def visit(self, stages: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetLeadsV3RequestView.STAGES:
            return stages()
