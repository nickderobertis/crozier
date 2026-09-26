

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sparks import Sparks


class WeeklyMetricsResponse(UniversalBaseModel):
    api_spend_usd_mtd: float
    avg_compliance: typing.Optional[float] = None
    avg_manual_edit_min: typing.Optional[float] = None
    kits_this_week: int
    sparks: Sparks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
