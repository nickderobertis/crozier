

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommonTpid(enum.StrEnum):
    HUBSPOT = "hubspot"
    ZOHOCRM = "zohocrm"
    SFDC = "sfdc"
    PIPEDRIVE = "pipedrive"
    SLACK = "slack"
    CLOSECRM = "closecrm"
    MS_DYNAMICS365SALES = "ms_dynamics_365_sales"

    def visit(
        self,
        hubspot: typing.Callable[[], T_Result],
        zohocrm: typing.Callable[[], T_Result],
        sfdc: typing.Callable[[], T_Result],
        pipedrive: typing.Callable[[], T_Result],
        slack: typing.Callable[[], T_Result],
        closecrm: typing.Callable[[], T_Result],
        ms_dynamics365sales: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommonTpid.HUBSPOT:
            return hubspot()
        if self is CommonTpid.ZOHOCRM:
            return zohocrm()
        if self is CommonTpid.SFDC:
            return sfdc()
        if self is CommonTpid.PIPEDRIVE:
            return pipedrive()
        if self is CommonTpid.SLACK:
            return slack()
        if self is CommonTpid.CLOSECRM:
            return closecrm()
        if self is CommonTpid.MS_DYNAMICS365SALES:
            return ms_dynamics365sales()
