

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .player_heartbeat_noise_meter_pending_history_item import PlayerHeartbeatNoiseMeterPendingHistoryItem
from .player_heartbeat_noise_meter_status import PlayerHeartbeatNoiseMeterStatus


class PlayerHeartbeatNoiseMeter(UniversalBaseModel):
    """
    Noise Meter plugin state. Contains no audio, waveform, or sample, and levels are the relative 0-100 Tilecast scale rather than dB, dBA, or SPL.
    """

    status: typing.Optional[PlayerHeartbeatNoiseMeterStatus] = None
    current_level: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="currentLevel"),
        pydantic.Field(alias="currentLevel", description="The live relative level when the heartbeat was built."),
    ] = None
    """
    The live relative level when the heartbeat was built.
    """

    pending_history: typing_extensions.Annotated[
        typing.Optional[typing.List[PlayerHeartbeatNoiseMeterPendingHistoryItem]],
        FieldMetadata(alias="pendingHistory"),
        pydantic.Field(
            alias="pendingHistory",
            description="The oldest unacknowledged ten-second buckets. Bounded per heartbeat; the rest stay queued on the Player for later heartbeats rather than accelerating the cadence.",
        ),
    ] = None
    """
    The oldest unacknowledged ten-second buckets. Bounded per heartbeat; the rest stay queued on the Player for later heartbeats rather than accelerating the cadence.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
