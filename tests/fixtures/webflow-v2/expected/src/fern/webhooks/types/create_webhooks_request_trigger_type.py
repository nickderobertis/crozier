

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateWebhooksRequestTriggerType(enum.StrEnum):
    """
    The type of event that triggered the request. See the the documentation for details on [supported events](/data/reference/all-events).
    """

    FORM_SUBMISSION = "form_submission"
    SITE_PUBLISH = "site_publish"
    PAGE_CREATED = "page_created"
    PAGE_METADATA_UPDATED = "page_metadata_updated"
    PAGE_DELETED = "page_deleted"
    ECOMM_NEW_ORDER = "ecomm_new_order"
    ECOMM_ORDER_CHANGED = "ecomm_order_changed"
    ECOMM_INVENTORY_CHANGED = "ecomm_inventory_changed"
    COLLECTION_ITEM_CREATED = "collection_item_created"
    COLLECTION_ITEM_CHANGED = "collection_item_changed"
    COLLECTION_ITEM_DELETED = "collection_item_deleted"
    COLLECTION_ITEM_PUBLISHED = "collection_item_published"
    COLLECTION_ITEM_UNPUBLISHED = "collection_item_unpublished"
    COMMENT_CREATED = "comment_created"

    def visit(
        self,
        form_submission: typing.Callable[[], T_Result],
        site_publish: typing.Callable[[], T_Result],
        page_created: typing.Callable[[], T_Result],
        page_metadata_updated: typing.Callable[[], T_Result],
        page_deleted: typing.Callable[[], T_Result],
        ecomm_new_order: typing.Callable[[], T_Result],
        ecomm_order_changed: typing.Callable[[], T_Result],
        ecomm_inventory_changed: typing.Callable[[], T_Result],
        collection_item_created: typing.Callable[[], T_Result],
        collection_item_changed: typing.Callable[[], T_Result],
        collection_item_deleted: typing.Callable[[], T_Result],
        collection_item_published: typing.Callable[[], T_Result],
        collection_item_unpublished: typing.Callable[[], T_Result],
        comment_created: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateWebhooksRequestTriggerType.FORM_SUBMISSION:
            return form_submission()
        if self is CreateWebhooksRequestTriggerType.SITE_PUBLISH:
            return site_publish()
        if self is CreateWebhooksRequestTriggerType.PAGE_CREATED:
            return page_created()
        if self is CreateWebhooksRequestTriggerType.PAGE_METADATA_UPDATED:
            return page_metadata_updated()
        if self is CreateWebhooksRequestTriggerType.PAGE_DELETED:
            return page_deleted()
        if self is CreateWebhooksRequestTriggerType.ECOMM_NEW_ORDER:
            return ecomm_new_order()
        if self is CreateWebhooksRequestTriggerType.ECOMM_ORDER_CHANGED:
            return ecomm_order_changed()
        if self is CreateWebhooksRequestTriggerType.ECOMM_INVENTORY_CHANGED:
            return ecomm_inventory_changed()
        if self is CreateWebhooksRequestTriggerType.COLLECTION_ITEM_CREATED:
            return collection_item_created()
        if self is CreateWebhooksRequestTriggerType.COLLECTION_ITEM_CHANGED:
            return collection_item_changed()
        if self is CreateWebhooksRequestTriggerType.COLLECTION_ITEM_DELETED:
            return collection_item_deleted()
        if self is CreateWebhooksRequestTriggerType.COLLECTION_ITEM_PUBLISHED:
            return collection_item_published()
        if self is CreateWebhooksRequestTriggerType.COLLECTION_ITEM_UNPUBLISHED:
            return collection_item_unpublished()
        if self is CreateWebhooksRequestTriggerType.COMMENT_CREATED:
            return comment_created()
