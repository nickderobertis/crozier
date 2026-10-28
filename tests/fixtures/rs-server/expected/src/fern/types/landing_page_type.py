

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LandingPageType(enum.StrEnum):
    CATALOG = "Catalog"

    def visit(self, catalog: typing.Callable[[], T_Result]) -> T_Result:
        if self is LandingPageType.CATALOG:
            return catalog()
