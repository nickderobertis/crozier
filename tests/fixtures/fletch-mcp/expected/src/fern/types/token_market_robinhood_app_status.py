

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenMarketRobinhoodAppStatus(enum.StrEnum):
    TRADABLE = "tradable"
    DISPLAY_ONLY = "display_only"
    NOT_IN_APP = "not_in_app"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        tradable: typing.Callable[[], T_Result],
        display_only: typing.Callable[[], T_Result],
        not_in_app: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TokenMarketRobinhoodAppStatus.TRADABLE:
            return tradable()
        if self is TokenMarketRobinhoodAppStatus.DISPLAY_ONLY:
            return display_only()
        if self is TokenMarketRobinhoodAppStatus.NOT_IN_APP:
            return not_in_app()
        if self is TokenMarketRobinhoodAppStatus.UNAVAILABLE:
            return unavailable()
