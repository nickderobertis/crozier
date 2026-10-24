

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schedule_evidence_selectors_item import ScheduleEvidenceSelectorsItem


class Schedule(UniversalBaseModel):
    id: str
    tenant_id: str
    name: str
    objective: str
    evidence_import_ids: typing.List[str]
    evidence_selectors: typing.List[ScheduleEvidenceSelectorsItem]
    interval_minutes: int
    enabled: bool
    next_run_at: dt.datetime
    lease_until: typing.Optional[dt.datetime] = None
    created_by: str
    created_at: dt.datetime
    updated_at: dt.datetime
    last_run_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
