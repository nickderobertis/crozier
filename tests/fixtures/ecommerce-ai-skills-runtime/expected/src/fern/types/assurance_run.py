

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assurance_check import AssuranceCheck
from .assurance_run_kind import AssuranceRunKind
from .assurance_run_status import AssuranceRunStatus
from .assurance_summary import AssuranceSummary


class AssuranceRun(UniversalBaseModel):
    id: str
    tenant_id: str
    kind: AssuranceRunKind
    idempotency_key: str
    status: AssuranceRunStatus
    actor_user_id: typing.Optional[str] = None
    checks: typing.List[AssuranceCheck]
    summary: AssuranceSummary
    created_at: dt.datetime
    lease_until: typing.Optional[dt.datetime] = None
    attempt_count: int
    completed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
