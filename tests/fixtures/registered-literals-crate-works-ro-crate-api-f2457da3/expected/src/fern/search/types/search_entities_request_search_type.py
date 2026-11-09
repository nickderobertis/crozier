

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchEntitiesRequestSearchType(enum.StrEnum):
    """
    Specifies the search method to be used. `basic` searches across common fields, whereas `advanced` can handle Boolean queries or more complex logic.
    """

    BASIC = "basic"
    ADVANCED = "advanced"

    def visit(self, basic: typing.Callable[[], T_Result], advanced: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchEntitiesRequestSearchType.BASIC:
            return basic()
        if self is SearchEntitiesRequestSearchType.ADVANCED:
            return advanced()
