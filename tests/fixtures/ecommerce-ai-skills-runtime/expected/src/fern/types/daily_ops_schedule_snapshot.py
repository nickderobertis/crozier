

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .daily_ops_evidence_selector import DailyOpsEvidenceSelector
from .marketplace_id import MarketplaceId


class DailyOpsScheduleSnapshot(UniversalBaseModel):
    schema_version: int
    tenant_id: str
    schedule_id: str
    name: str
    platform: MarketplaceId
    objective: str
    timezone: str
    local_time: str
    local_date: dt.date
    scheduled_for: dt.datetime
    graph_version_id: str
    graph_version_hash: str
    evidence_selectors: typing.List[DailyOpsEvidenceSelector]
    max_source_age_hours: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
