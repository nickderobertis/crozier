

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_watchers_response_watchers_item_delivery import GetWatchersResponseWatchersItemDelivery
from .get_watchers_response_watchers_item_kind import GetWatchersResponseWatchersItemKind
from .get_watchers_response_watchers_item_last_delivery import GetWatchersResponseWatchersItemLastDelivery
from .get_watchers_response_watchers_item_status import GetWatchersResponseWatchersItemStatus


class GetWatchersResponseWatchersItem(UniversalBaseModel):
    id: str
    project_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="projectId"), pydantic.Field(alias="projectId")
    ] = None
    name: str
    kind: GetWatchersResponseWatchersItemKind
    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    address: str
    asset_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assetId"), pydantic.Field(alias="assetId")
    ] = None
    threshold: str
    wallet: typing.Optional[str] = pydantic.Field(default=None)
    """
    wallet_activity only — the watched address.
    """

    delivery: typing.Optional[GetWatchersResponseWatchersItemDelivery] = pydantic.Field(default=None)
    """
    Where this watcher's alerts are sent.
    """

    webhook_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webhookId"),
        pydantic.Field(alias="webhookId", description='The endpoint alerts are posted to when delivery is "webhook".'),
    ] = None
    """
    The endpoint alerts are posted to when delivery is "webhook".
    """

    webhook_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webhookName"),
        pydantic.Field(
            alias="webhookName",
            description='The endpoint\'s name. Null when delivery is "telegram". Also null when the endpoint was deleted: delivery stays "webhook", webhookId is null, and the watcher is paused with the reason in lastError. Such a watcher cannot be resumed until it is re-pointed with PATCH /watchers/{id} { webhookId }.',
        ),
    ] = None
    """
    The endpoint's name. Null when delivery is "telegram". Also null when the endpoint was deleted: delivery stays "webhook", webhookId is null, and the watcher is paused with the reason in lastError. Such a watcher cannot be resumed until it is re-pointed with PATCH /watchers/{id} { webhookId }.
    """

    enabled: bool
    status: GetWatchersResponseWatchersItemStatus
    last_checked_block: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastCheckedBlock"), pydantic.Field(alias="lastCheckedBlock")
    ] = None
    last_triggered_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastTriggeredAt"), pydantic.Field(alias="lastTriggeredAt")
    ] = None
    last_error: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastError"), pydantic.Field(alias="lastError")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    last_delivery: typing_extensions.Annotated[
        typing.Optional[GetWatchersResponseWatchersItemLastDelivery],
        FieldMetadata(alias="lastDelivery"),
        pydantic.Field(
            alias="lastDelivery", description="The most recent delivery of any status, or null before the first."
        ),
    ] = None
    """
    The most recent delivery of any status, or null before the first.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
