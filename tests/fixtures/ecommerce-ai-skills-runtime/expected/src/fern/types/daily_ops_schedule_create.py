

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .daily_ops_evidence_selector import DailyOpsEvidenceSelector
from .marketplace_id import MarketplaceId


class DailyOpsScheduleCreate(UniversalBaseModel):
    name: str
    platform: MarketplaceId
    objective: str
    timezone_name: str = pydantic.Field()
    """
    IANA timezone name, for example `America/Los_Angeles`.
    """

    local_time: str = pydantic.Field()
    """
    24-hour wall-clock time in timezone_name.
    """

    graph_version_id: str
    evidence_selectors: typing.List[DailyOpsEvidenceSelector]
    max_source_age_hours: typing.Optional[int] = None
    enabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
