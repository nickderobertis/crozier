

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_blocker import PilotBlocker
from .pilot_runtime_status import PilotRuntimeStatus
from .pilot_status_status import PilotStatusStatus
from .pilot_tenant_readiness import PilotTenantReadiness


class PilotStatus(UniversalBaseModel):
    """
    Closed operational snapshot for the authenticated tenant; it is not proof that Amazon or OpenAI calls work.
    """

    status: PilotStatusStatus
    blockers: typing.List[PilotBlocker]
    warnings: typing.List[PilotBlocker]
    runtime: PilotRuntimeStatus
    tenant: PilotTenantReadiness

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
