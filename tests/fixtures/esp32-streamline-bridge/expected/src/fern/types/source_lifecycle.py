

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .source_lifecycle_admission import SourceLifecycleAdmission
from .source_lifecycle_state import SourceLifecycleState
from .source_lifecycle_transport import SourceLifecycleTransport


class SourceLifecycle(UniversalBaseModel):
    admission: SourceLifecycleAdmission
    dynamic: bool
    eviction_idle_seconds: typing.Optional[float] = None
    http_clients: int
    idle_seconds: float
    peer_ip: str
    recording_sessions: int
    state: SourceLifecycleState
    transport: SourceLifecycleTransport

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
