

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .evidence_report_type import EvidenceReportType


class OperatingBriefingEvidence(UniversalBaseModel):
    source_count: int
    row_count: int
    latest_observed_at: typing.Optional[dt.datetime] = None
    report_types: typing.List[EvidenceReportType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
