

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_snapshot import ClientSnapshot
from .level_snapshot import LevelSnapshot
from .source_lifecycle import SourceLifecycle


class SourceSnapshot(UniversalBaseModel):
    buffer_ready_at: typing.Optional[float] = None
    buffered_packets: int
    bytes: int
    client_buffer_chunks: int
    client_queue_drops: int
    client_streams: typing.List[ClientSnapshot]
    clients: int
    concealed: int
    duplicate: int
    frames: int
    highest_seq: typing.Optional[int] = None
    last_packet_at: typing.Optional[float] = None
    last_playout_at: typing.Optional[float] = None
    last_seq: typing.Optional[int] = None
    late: int
    levels: LevelSnapshot
    lifecycle: SourceLifecycle
    lost: int
    max_buffered_packets: int
    max_outage_silence_packets: int
    overflows: int
    packet_frames: typing.Optional[int] = None
    packets: int
    played_frames: int
    playout_buffer_packets: int
    playout_seq: typing.Optional[int] = None
    rate: int
    reordered: int
    slow_clients: int
    started_at: float
    tcp_connections: int
    tcp_disconnects: int
    tcp_errors: int
    underruns: int
    uptime_seconds: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
