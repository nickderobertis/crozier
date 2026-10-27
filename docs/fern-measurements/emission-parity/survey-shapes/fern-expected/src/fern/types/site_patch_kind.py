

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SitePatchKind(enum.StrEnum):
    SITE = "Site"

    def visit(self, site: typing.Callable[[], T_Result]) -> T_Result:
        if self is SitePatchKind.SITE:
            return site()
