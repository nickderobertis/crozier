

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataNullishEightType(enum.StrEnum):
    TOPIC_MAP = "topic_map"

    def visit(self, topic_map: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataNullishEightType.TOPIC_MAP:
            return topic_map()
