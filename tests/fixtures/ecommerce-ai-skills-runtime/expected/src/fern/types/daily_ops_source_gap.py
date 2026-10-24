

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .daily_ops_source_gap_verdict import DailyOpsSourceGapVerdict
from .evidence_report_type import EvidenceReportType
from .marketplace_id import MarketplaceId


class DailyOpsSourceGap(UniversalBaseModel):
    code: str
    platform: typing.Optional[MarketplaceId] = None
    report_type: typing.Optional[EvidenceReportType] = None
    as_of: typing.Optional[dt.datetime] = None
    max_source_age_hours: typing.Optional[int] = None
    local_time: typing.Optional[str] = None
    verdict: typing.Optional[DailyOpsSourceGapVerdict] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
