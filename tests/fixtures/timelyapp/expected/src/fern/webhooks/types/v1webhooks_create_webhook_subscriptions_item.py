

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1WebhooksCreateWebhookSubscriptionsItem(enum.StrEnum):
    FORECASTS_CREATED = "forecasts:created"
    FORECASTS_UPDATED = "forecasts:updated"
    FORECASTS_DELETED = "forecasts:deleted"
    HOURS_CREATED = "hours:created"
    HOURS_UPDATED = "hours:updated"
    HOURS_DELETED = "hours:deleted"
    LABELS_CREATED = "labels:created"
    LABELS_UPDATED = "labels:updated"
    LABELS_DELETED = "labels:deleted"
    PROJECTS_CREATED = "projects:created"
    PROJECTS_UPDATED = "projects:updated"
    PROJECTS_DELETED = "projects:deleted"

    def visit(
        self,
        forecasts_created: typing.Callable[[], T_Result],
        forecasts_updated: typing.Callable[[], T_Result],
        forecasts_deleted: typing.Callable[[], T_Result],
        hours_created: typing.Callable[[], T_Result],
        hours_updated: typing.Callable[[], T_Result],
        hours_deleted: typing.Callable[[], T_Result],
        labels_created: typing.Callable[[], T_Result],
        labels_updated: typing.Callable[[], T_Result],
        labels_deleted: typing.Callable[[], T_Result],
        projects_created: typing.Callable[[], T_Result],
        projects_updated: typing.Callable[[], T_Result],
        projects_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1WebhooksCreateWebhookSubscriptionsItem.FORECASTS_CREATED:
            return forecasts_created()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.FORECASTS_UPDATED:
            return forecasts_updated()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.FORECASTS_DELETED:
            return forecasts_deleted()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.HOURS_CREATED:
            return hours_created()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.HOURS_UPDATED:
            return hours_updated()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.HOURS_DELETED:
            return hours_deleted()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.LABELS_CREATED:
            return labels_created()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.LABELS_UPDATED:
            return labels_updated()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.LABELS_DELETED:
            return labels_deleted()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.PROJECTS_CREATED:
            return projects_created()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.PROJECTS_UPDATED:
            return projects_updated()
        if self is V1WebhooksCreateWebhookSubscriptionsItem.PROJECTS_DELETED:
            return projects_deleted()
