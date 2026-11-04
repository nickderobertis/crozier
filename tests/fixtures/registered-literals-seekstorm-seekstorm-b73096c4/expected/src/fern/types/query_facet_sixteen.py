

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryFacetSixteen(enum.StrEnum):
    """
    No query facet
    """

    NONE = "None"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryFacetSixteen.NONE:
            return none()
