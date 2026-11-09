

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Source(enum.StrEnum):
    """
    A type indicating whether a dashboard user, an API-based user, or Plaid last touched this object.
    """

    DASHBOARD = "dashboard"
    LINK = "link"
    API = "api"
    SYSTEM = "system"

    def visit(
        self,
        dashboard: typing.Callable[[], T_Result],
        link: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Source.DASHBOARD:
            return dashboard()
        if self is Source.LINK:
            return link()
        if self is Source.API:
            return api()
        if self is Source.SYSTEM:
            return system()
