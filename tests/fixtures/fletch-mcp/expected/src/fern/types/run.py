

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .run_status import RunStatus


class Run(UniversalBaseModel):
    id: str
    watcher_id: typing_extensions.Annotated[str, FieldMetadata(alias="watcherId"), pydantic.Field(alias="watcherId")]
    status: RunStatus
    last_error: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastError"), pydantic.Field(alias="lastError")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    sent_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="sentAt"), pydantic.Field(alias="sentAt")
    ] = None
    payload: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    DeliveryPayload — kind, chainId, address, symbol, from, to, value, amount, threshold, txHash, logIndex, blockNumber, blockHash, explorerUrl; wallet_activity adds wallet and direction ("in" | "out"); an authority payload (kind "authority", from a registry_event or token_event watcher) instead carries eventId, eventKind, title, symbol, address, detail, txHash, blockNumber, occurredAt (ISO 8601 UTC), explorerUrl and registryUrl.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
