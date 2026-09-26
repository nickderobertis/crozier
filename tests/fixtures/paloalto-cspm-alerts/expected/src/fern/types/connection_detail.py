

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConnectionDetail(UniversalBaseModel):
    accepted: typing.Optional[str] = None
    account_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accountName"), pydantic.Field(alias="accountName")
    ] = None
    classification: typing.Optional[str] = None
    dest_ip: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="destIp"), pydantic.Field(alias="destIp")
    ] = None
    dest_isp: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="destIsp"), pydantic.Field(alias="destIsp")
    ] = None
    feed_source: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="feedSource"), pydantic.Field(alias="feedSource")
    ] = None
    id: typing.Optional[int] = None
    inbound_traffic_volume: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="inboundTrafficVolume"), pydantic.Field(alias="inboundTrafficVolume")
    ] = None
    marked_threat_ts: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="markedThreatTs"), pydantic.Field(alias="markedThreatTs")
    ] = None
    outbound_traffic_volume: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="outboundTrafficVolume"),
        pydantic.Field(alias="outboundTrafficVolume"),
    ] = None
    packets: typing.Optional[int] = None
    src_ip: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="srcIp"), pydantic.Field(alias="srcIp")
    ] = None
    src_isp: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="srcIsp"), pydantic.Field(alias="srcIsp")
    ] = None
    threat_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="threatDescription"), pydantic.Field(alias="threatDescription")
    ] = None
    timestamp: typing.Optional[int] = None
    traffic_over_time: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, int]]],
        FieldMetadata(alias="trafficOverTime"),
        pydantic.Field(alias="trafficOverTime"),
    ] = None
    traffic_volume: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="trafficVolume"), pydantic.Field(alias="trafficVolume")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
