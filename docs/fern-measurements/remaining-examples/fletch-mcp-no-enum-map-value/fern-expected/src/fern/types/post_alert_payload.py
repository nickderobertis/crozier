

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .post_alert_payload_kind import PostAlertPayloadKind
from .post_alert_payload_watcher import PostAlertPayloadWatcher


class PostAlertPayload(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Delivery id, `dl_…` (`ping_…` for a test); the idempotency key.
    """

    kind: PostAlertPayloadKind
    payload: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    DeliveryPayload — kind, chainId, address, symbol, from, to, value, amount, threshold, txHash, logIndex, blockNumber, blockHash, explorerUrl; wallet_activity adds wallet and direction ("in" | "out"); an authority payload (kind "authority", from a registry_event or token_event watcher) instead carries eventId, eventKind, title, symbol, address, detail, txHash, blockNumber, occurredAt (ISO 8601 UTC), explorerUrl and registryUrl.
    """

    watcher: typing.Optional[PostAlertPayloadWatcher] = pydantic.Field(default=None)
    """
    null for a ping, which belongs to the endpoint rather than to any watcher.
    """

    queued_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="queuedAt"),
        pydantic.Field(
            alias="queuedAt", description="When Fletch matched the event. On a retry this is well before sentAt."
        ),
    ]
    """
    When Fletch matched the event. On a retry this is well before sentAt.
    """

    attempt: int = pydantic.Field()
    """
    1 on the first try.
    """

    sent_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="sentAt"),
        pydantic.Field(alias="sentAt", description="When this attempt was posted."),
    ]
    """
    When this attempt was posted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
