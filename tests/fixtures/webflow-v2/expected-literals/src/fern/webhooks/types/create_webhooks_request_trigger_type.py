

import typing

CreateWebhooksRequestTriggerType = typing.Union[
    typing.Literal[
        "form_submission",
        "site_publish",
        "page_created",
        "page_metadata_updated",
        "page_deleted",
        "ecomm_new_order",
        "ecomm_order_changed",
        "ecomm_inventory_changed",
        "collection_item_created",
        "collection_item_changed",
        "collection_item_deleted",
        "collection_item_published",
        "collection_item_unpublished",
        "comment_created",
    ],
    typing.Any,
]
