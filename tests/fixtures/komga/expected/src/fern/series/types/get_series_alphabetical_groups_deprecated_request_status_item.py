

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem(enum.StrEnum):
    ENDED = "ENDED"
    ONGOING = "ONGOING"
    ABANDONED = "ABANDONED"
    HIATUS = "HIATUS"

    def visit(
        self,
        ended: typing.Callable[[], T_Result],
        ongoing: typing.Callable[[], T_Result],
        abandoned: typing.Callable[[], T_Result],
        hiatus: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem.ENDED:
            return ended()
        if self is GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem.ONGOING:
            return ongoing()
        if self is GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem.ABANDONED:
            return abandoned()
        if self is GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem.HIATUS:
            return hiatus()
