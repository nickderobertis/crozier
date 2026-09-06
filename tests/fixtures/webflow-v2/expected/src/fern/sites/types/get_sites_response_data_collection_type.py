

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSitesResponseDataCollectionType(enum.StrEnum):
    """
    The type of data collection enabled for the site.
    """

    ALWAYS = "always"
    OPT_OUT = "optOut"
    DISABLED = "disabled"

    def visit(
        self,
        always: typing.Callable[[], T_Result],
        opt_out: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSitesResponseDataCollectionType.ALWAYS:
            return always()
        if self is GetSitesResponseDataCollectionType.OPT_OUT:
            return opt_out()
        if self is GetSitesResponseDataCollectionType.DISABLED:
            return disabled()
