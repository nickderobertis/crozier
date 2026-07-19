

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookEventsItem(enum.StrEnum):
    FLOWS_CREATED = "flows/created"
    FLOWS_UPDATED = "flows/updated"
    FLOWS_DELETED = "flows/deleted"
    FLOWS_SEGMENTS_ADDED = "flows/segments_added"
    FLOWS_SEGMENTS_DELETED = "flows/segments_deleted"
    SOURCES_CREATED = "sources/created"
    SOURCES_UPDATED = "sources/updated"
    SOURCES_DELETED = "sources/deleted"

    def visit(
        self,
        flows_created: typing.Callable[[], T_Result],
        flows_updated: typing.Callable[[], T_Result],
        flows_deleted: typing.Callable[[], T_Result],
        flows_segments_added: typing.Callable[[], T_Result],
        flows_segments_deleted: typing.Callable[[], T_Result],
        sources_created: typing.Callable[[], T_Result],
        sources_updated: typing.Callable[[], T_Result],
        sources_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookEventsItem.FLOWS_CREATED:
            return flows_created()
        if self is WebhookEventsItem.FLOWS_UPDATED:
            return flows_updated()
        if self is WebhookEventsItem.FLOWS_DELETED:
            return flows_deleted()
        if self is WebhookEventsItem.FLOWS_SEGMENTS_ADDED:
            return flows_segments_added()
        if self is WebhookEventsItem.FLOWS_SEGMENTS_DELETED:
            return flows_segments_deleted()
        if self is WebhookEventsItem.SOURCES_CREATED:
            return sources_created()
        if self is WebhookEventsItem.SOURCES_UPDATED:
            return sources_updated()
        if self is WebhookEventsItem.SOURCES_DELETED:
            return sources_deleted()
