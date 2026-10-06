

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BattlesControllerGetRatingDeltaByOpponentRequestPeriod(enum.StrEnum):
    TWENTY_FOUR_H = "24h"
    THREE_D = "3d"
    SEVEN_D = "7d"
    FOURTEEN_D = "14d"
    THIRTY_D = "30d"
    NINETY_D = "90d"
    ONE_HUNDRED_EIGHTY_D = "180d"
    ALL = "all"

    def visit(
        self,
        twenty_four_h: typing.Callable[[], T_Result],
        three_d: typing.Callable[[], T_Result],
        seven_d: typing.Callable[[], T_Result],
        fourteen_d: typing.Callable[[], T_Result],
        thirty_d: typing.Callable[[], T_Result],
        ninety_d: typing.Callable[[], T_Result],
        one_hundred_eighty_d: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.TWENTY_FOUR_H:
            return twenty_four_h()
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.THREE_D:
            return three_d()
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.SEVEN_D:
            return seven_d()
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.FOURTEEN_D:
            return fourteen_d()
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.THIRTY_D:
            return thirty_d()
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.NINETY_D:
            return ninety_d()
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.ONE_HUNDRED_EIGHTY_D:
            return one_hundred_eighty_d()
        if self is BattlesControllerGetRatingDeltaByOpponentRequestPeriod.ALL:
            return all_()
