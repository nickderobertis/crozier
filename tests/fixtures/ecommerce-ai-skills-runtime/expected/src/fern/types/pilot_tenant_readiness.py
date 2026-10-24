

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_blocker import PilotBlocker
from .pilot_tenant_components import PilotTenantComponents
from .pilot_tenant_readiness_status import PilotTenantReadinessStatus
from .pilot_tenant_readiness_tenant_mode import PilotTenantReadinessTenantMode


class PilotTenantReadiness(UniversalBaseModel):
    tenant_id: str
    tenant_name: str
    tenant_mode: PilotTenantReadinessTenantMode
    status: PilotTenantReadinessStatus
    blockers: typing.List[PilotBlocker]
    components: PilotTenantComponents

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
