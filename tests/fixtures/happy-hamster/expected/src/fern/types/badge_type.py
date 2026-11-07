

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadgeType(enum.StrEnum):
    """
    Badges for certain actions
    """

    NEXT_LEVEL = "next_level"
    NEXT_LEVEL_CLASS = "next_level_class"
    REPORT = "report"
    NEW_REPORT = "new_report"
    TWO_SHOPS = "two_shops"
    SHOP_FIRST_REPORT = "shop_first_report"
    WEEK1 = "week_1"
    WEEK3 = "week_3"
    WEEK_FULL = "week_full"
    WEEK_SPECIAL = "week_special"
    TRUSTED_SHOP = "trusted_shop"
    TRUSTED_USER = "trusted_user"

    def visit(
        self,
        next_level: typing.Callable[[], T_Result],
        next_level_class: typing.Callable[[], T_Result],
        report: typing.Callable[[], T_Result],
        new_report: typing.Callable[[], T_Result],
        two_shops: typing.Callable[[], T_Result],
        shop_first_report: typing.Callable[[], T_Result],
        week1: typing.Callable[[], T_Result],
        week3: typing.Callable[[], T_Result],
        week_full: typing.Callable[[], T_Result],
        week_special: typing.Callable[[], T_Result],
        trusted_shop: typing.Callable[[], T_Result],
        trusted_user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BadgeType.NEXT_LEVEL:
            return next_level()
        if self is BadgeType.NEXT_LEVEL_CLASS:
            return next_level_class()
        if self is BadgeType.REPORT:
            return report()
        if self is BadgeType.NEW_REPORT:
            return new_report()
        if self is BadgeType.TWO_SHOPS:
            return two_shops()
        if self is BadgeType.SHOP_FIRST_REPORT:
            return shop_first_report()
        if self is BadgeType.WEEK1:
            return week1()
        if self is BadgeType.WEEK3:
            return week3()
        if self is BadgeType.WEEK_FULL:
            return week_full()
        if self is BadgeType.WEEK_SPECIAL:
            return week_special()
        if self is BadgeType.TRUSTED_SHOP:
            return trusted_shop()
        if self is BadgeType.TRUSTED_USER:
            return trusted_user()
