

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyBodyAllOfType(enum.StrEnum):
    ALL_OF = "ALL_OF"

    def visit(self, all_of: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyBodyAllOfType.ALL_OF:
            return all_of()
