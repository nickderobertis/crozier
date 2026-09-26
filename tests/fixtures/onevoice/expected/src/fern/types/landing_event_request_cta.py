

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LandingEventRequestCta(enum.StrEnum):
    HERO_WAITLIST = "hero-waitlist"
    HERO_REGISTER = "hero-register"
    NAV_REGISTER = "nav-register"
    NAV_LOGIN = "nav-login"
    PRICING_FREE_REGISTER = "pricing-free-register"
    PRICING_PRO_WAITLIST = "pricing-pro-waitlist"
    WAITLIST_SUCCESS_REGISTER = "waitlist-success-register"

    def visit(
        self,
        hero_waitlist: typing.Callable[[], T_Result],
        hero_register: typing.Callable[[], T_Result],
        nav_register: typing.Callable[[], T_Result],
        nav_login: typing.Callable[[], T_Result],
        pricing_free_register: typing.Callable[[], T_Result],
        pricing_pro_waitlist: typing.Callable[[], T_Result],
        waitlist_success_register: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LandingEventRequestCta.HERO_WAITLIST:
            return hero_waitlist()
        if self is LandingEventRequestCta.HERO_REGISTER:
            return hero_register()
        if self is LandingEventRequestCta.NAV_REGISTER:
            return nav_register()
        if self is LandingEventRequestCta.NAV_LOGIN:
            return nav_login()
        if self is LandingEventRequestCta.PRICING_FREE_REGISTER:
            return pricing_free_register()
        if self is LandingEventRequestCta.PRICING_PRO_WAITLIST:
            return pricing_pro_waitlist()
        if self is LandingEventRequestCta.WAITLIST_SUCCESS_REGISTER:
            return waitlist_success_register()
