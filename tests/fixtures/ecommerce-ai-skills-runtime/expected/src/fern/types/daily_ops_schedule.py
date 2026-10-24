

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .daily_ops_evidence_selector import DailyOpsEvidenceSelector
from .marketplace_id import MarketplaceId


class DailyOpsSchedule(UniversalBaseModel):
    id: str
    tenant_id: str
    name: str
    platform: MarketplaceId
    objective: str
    timezone: str
    local_time: str
    graph_version_id: str
    evidence_selectors: typing.List[DailyOpsEvidenceSelector]
    max_source_age_hours: int
    enabled: bool
    next_local_date: dt.date = pydantic.Field()
    """
    Durable calendar cursor; the scheduler catches up one due local date per invocation.
    """

    created_by: str
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
