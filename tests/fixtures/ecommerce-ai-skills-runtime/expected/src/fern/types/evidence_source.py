

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .evidence_source_data import EvidenceSourceData
from .platform_id import PlatformId


class EvidenceSource(UniversalBaseModel):
    source_id: str
    platform: PlatformId
    source_type: str
    observed_at: dt.datetime
    data: EvidenceSourceData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
