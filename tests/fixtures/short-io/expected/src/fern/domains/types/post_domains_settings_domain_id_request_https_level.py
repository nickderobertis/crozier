

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostDomainsSettingsDomainIdRequestHttpsLevel(enum.StrEnum):
    NONE = "none"
    REDIRECT = "redirect"
    HSTS = "hsts"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        redirect: typing.Callable[[], T_Result],
        hsts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostDomainsSettingsDomainIdRequestHttpsLevel.NONE:
            return none()
        if self is PostDomainsSettingsDomainIdRequestHttpsLevel.REDIRECT:
            return redirect()
        if self is PostDomainsSettingsDomainIdRequestHttpsLevel.HSTS:
            return hsts()
