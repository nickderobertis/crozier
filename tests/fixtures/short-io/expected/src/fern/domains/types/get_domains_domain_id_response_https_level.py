

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDomainsDomainIdResponseHttpsLevel(enum.StrEnum):
    NONE = "none"
    REDIRECT = "redirect"
    HSTS = "hsts"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        redirect: typing.Callable[[], T_Result],
        hsts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDomainsDomainIdResponseHttpsLevel.NONE:
            return none()
        if self is GetDomainsDomainIdResponseHttpsLevel.REDIRECT:
            return redirect()
        if self is GetDomainsDomainIdResponseHttpsLevel.HSTS:
            return hsts()
