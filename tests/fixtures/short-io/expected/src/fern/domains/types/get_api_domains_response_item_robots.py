

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiDomainsResponseItemRobots(enum.StrEnum):
    ALLOW = "allow"
    DISALLOW = "disallow"
    NOINDEX = "noindex"

    def visit(
        self,
        allow: typing.Callable[[], T_Result],
        disallow: typing.Callable[[], T_Result],
        noindex: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiDomainsResponseItemRobots.ALLOW:
            return allow()
        if self is GetApiDomainsResponseItemRobots.DISALLOW:
            return disallow()
        if self is GetApiDomainsResponseItemRobots.NOINDEX:
            return noindex()
