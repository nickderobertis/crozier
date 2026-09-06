

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListActivityLogsResponseItemsItemResourceOperation(enum.StrEnum):
    CREATED = "CREATED"
    MODIFIED = "MODIFIED"
    PUBLISHED = "PUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"
    DELETED = "DELETED"
    GROUP_REORDERED = "GROUP_REORDERED"
    GROUP_CREATED = "GROUP_CREATED"
    GROUP_DELETED = "GROUP_DELETED"
    REORDERED = "REORDERED"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        modified: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        unpublished: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        group_reordered: typing.Callable[[], T_Result],
        group_created: typing.Callable[[], T_Result],
        group_deleted: typing.Callable[[], T_Result],
        reordered: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListActivityLogsResponseItemsItemResourceOperation.CREATED:
            return created()
        if self is ListActivityLogsResponseItemsItemResourceOperation.MODIFIED:
            return modified()
        if self is ListActivityLogsResponseItemsItemResourceOperation.PUBLISHED:
            return published()
        if self is ListActivityLogsResponseItemsItemResourceOperation.UNPUBLISHED:
            return unpublished()
        if self is ListActivityLogsResponseItemsItemResourceOperation.DELETED:
            return deleted()
        if self is ListActivityLogsResponseItemsItemResourceOperation.GROUP_REORDERED:
            return group_reordered()
        if self is ListActivityLogsResponseItemsItemResourceOperation.GROUP_CREATED:
            return group_created()
        if self is ListActivityLogsResponseItemsItemResourceOperation.GROUP_DELETED:
            return group_deleted()
        if self is ListActivityLogsResponseItemsItemResourceOperation.REORDERED:
            return reordered()
