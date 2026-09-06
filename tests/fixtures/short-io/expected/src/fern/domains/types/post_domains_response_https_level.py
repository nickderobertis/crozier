

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostDomainsResponseHttpsLevel(enum.StrEnum):
    NONE = "none"
    REDIRECT = "redirect"
    HSTS = "hsts"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        redirect: typing.Callable[[], T_Result],
        hsts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostDomainsResponseHttpsLevel.NONE:
            return none()
        if self is PostDomainsResponseHttpsLevel.REDIRECT:
            return redirect()
        if self is PostDomainsResponseHttpsLevel.HSTS:
            return hsts()
