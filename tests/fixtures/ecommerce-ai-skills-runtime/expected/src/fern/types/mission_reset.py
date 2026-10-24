

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mission_reset_reason import MissionResetReason
from .mission_reset_snapshot_url import MissionResetSnapshotUrl


class MissionReset(UniversalBaseModel):
    reason: MissionResetReason
    cursor: int
    snapshot_url: MissionResetSnapshotUrl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
