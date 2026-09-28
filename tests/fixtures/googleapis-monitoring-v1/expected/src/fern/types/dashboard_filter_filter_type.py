

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DashboardFilterFilterType(enum.StrEnum):
    """
    The specified filter type
    """

    FILTER_TYPE_UNSPECIFIED = "FILTER_TYPE_UNSPECIFIED"
    RESOURCE_LABEL = "RESOURCE_LABEL"
    METRIC_LABEL = "METRIC_LABEL"
    USER_METADATA_LABEL = "USER_METADATA_LABEL"
    SYSTEM_METADATA_LABEL = "SYSTEM_METADATA_LABEL"
    GROUP = "GROUP"

    def visit(
        self,
        filter_type_unspecified: typing.Callable[[], T_Result],
        resource_label: typing.Callable[[], T_Result],
        metric_label: typing.Callable[[], T_Result],
        user_metadata_label: typing.Callable[[], T_Result],
        system_metadata_label: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DashboardFilterFilterType.FILTER_TYPE_UNSPECIFIED:
            return filter_type_unspecified()
        if self is DashboardFilterFilterType.RESOURCE_LABEL:
            return resource_label()
        if self is DashboardFilterFilterType.METRIC_LABEL:
            return metric_label()
        if self is DashboardFilterFilterType.USER_METADATA_LABEL:
            return user_metadata_label()
        if self is DashboardFilterFilterType.SYSTEM_METADATA_LABEL:
            return system_metadata_label()
        if self is DashboardFilterFilterType.GROUP:
            return group()
