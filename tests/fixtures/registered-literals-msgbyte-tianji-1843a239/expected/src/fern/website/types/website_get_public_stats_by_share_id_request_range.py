

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebsiteGetPublicStatsByShareIdRequestRange(enum.StrEnum):
    REALTIME = "realtime"
    TWENTY_FOUR_H = "24h"
    SEVEN_D = "7d"
    THIRTY_D = "30d"
    NINETY_D = "90d"

    def visit(
        self,
        realtime: typing.Callable[[], T_Result],
        twenty_four_h: typing.Callable[[], T_Result],
        seven_d: typing.Callable[[], T_Result],
        thirty_d: typing.Callable[[], T_Result],
        ninety_d: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebsiteGetPublicStatsByShareIdRequestRange.REALTIME:
            return realtime()
        if self is WebsiteGetPublicStatsByShareIdRequestRange.TWENTY_FOUR_H:
            return twenty_four_h()
        if self is WebsiteGetPublicStatsByShareIdRequestRange.SEVEN_D:
            return seven_d()
        if self is WebsiteGetPublicStatsByShareIdRequestRange.THIRTY_D:
            return thirty_d()
        if self is WebsiteGetPublicStatsByShareIdRequestRange.NINETY_D:
            return ninety_d()
