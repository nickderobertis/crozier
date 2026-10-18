

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ServiceHealthResponseOutputInfoDescriptionName(enum.StrEnum):
    GO_TRUE = "GoTrue"

    def visit(self, go_true: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ServiceHealthResponseOutputInfoDescriptionName.GO_TRUE:
            return go_true()
