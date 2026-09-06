

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDomainsDomainIdResponseRobots(enum.StrEnum):
    ALLOW = "allow"
    DISALLOW = "disallow"
    NOINDEX = "noindex"

    def visit(
        self,
        allow: typing.Callable[[], T_Result],
        disallow: typing.Callable[[], T_Result],
        noindex: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDomainsDomainIdResponseRobots.ALLOW:
            return allow()
        if self is GetDomainsDomainIdResponseRobots.DISALLOW:
            return disallow()
        if self is GetDomainsDomainIdResponseRobots.NOINDEX:
            return noindex()
