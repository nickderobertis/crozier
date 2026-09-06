

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiDomainsResponseItemHttpsLevel(enum.StrEnum):
    NONE = "none"
    REDIRECT = "redirect"
    HSTS = "hsts"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        redirect: typing.Callable[[], T_Result],
        hsts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiDomainsResponseItemHttpsLevel.NONE:
            return none()
        if self is GetApiDomainsResponseItemHttpsLevel.REDIRECT:
            return redirect()
        if self is GetApiDomainsResponseItemHttpsLevel.HSTS:
            return hsts()
