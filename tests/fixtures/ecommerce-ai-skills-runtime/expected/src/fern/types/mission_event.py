

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mission_event_event_type import MissionEventEventType
from .mission_event_metadata import MissionEventMetadata
from .mission_event_resource_type import MissionEventResourceType


class MissionEvent(UniversalBaseModel):
    """
    Closed, tenant-safe `mission.update` data. It excludes the internal global sequence, tenant id, secrets, and resource payloads.
    """

    cursor: int
    event_type: MissionEventEventType
    resource_type: MissionEventResourceType
    resource_id: str
    status: str
    previous_status: typing.Optional[str] = None
    metadata: MissionEventMetadata = pydantic.Field()
    """
    Bounded safe relationship/status metadata only, never a resource representation.
    """

    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
