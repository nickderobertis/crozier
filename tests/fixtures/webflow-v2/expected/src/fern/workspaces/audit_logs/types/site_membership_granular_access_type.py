

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class SiteMembershipGranularAccessType(enum.StrEnum):
    CMS = "cms"

    def visit(self, cms: typing.Callable[[], T_Result]) -> T_Result:
        if self is SiteMembershipGranularAccessType.CMS:
            return cms()
