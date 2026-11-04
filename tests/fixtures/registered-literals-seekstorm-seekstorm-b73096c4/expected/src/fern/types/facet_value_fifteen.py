

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FacetValueFifteen(enum.StrEnum):
    """
    No value
    """

    NONE = "None"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is FacetValueFifteen.NONE:
            return none()
