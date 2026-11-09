

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GatewayPeer(UniversalBaseModel):
    address: str = pydantic.Field()
    """
    Peer network address.
    """

    inbound: bool = pydantic.Field()
    """
    Whether the connection was inbound.
    """

    version: str = pydantic.Field()
    """
    Peer-reported version.
    """

    first_seen: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="firstSeen"),
        pydantic.Field(alias="firstSeen", description="Time the peer was first observed, if known."),
    ] = None
    """
    Time the peer was first observed, if known.
    """

    connected_since: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="connectedSince"),
        pydantic.Field(alias="connectedSince", description="Time the peer connection was established."),
    ] = None
    """
    Time the peer connection was established.
    """

    synced_blocks: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="syncedBlocks"),
        pydantic.Field(alias="syncedBlocks", description="Number of blocks synced during the last session."),
    ] = None
    """
    Number of blocks synced during the last session.
    """

    sync_duration: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="syncDuration"),
        pydantic.Field(alias="syncDuration", description="Duration of the last sync, encoded as a Go duration string."),
    ] = None
    """
    Duration of the last sync, encoded as a Go duration string.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
