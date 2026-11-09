

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .daily_metrics_details import DailyMetricsDetails
from .utils_meta_response import UtilsMetaResponse


class DailyMetrics(UniversalBaseModel):
    data: typing.List[DailyMetricsDetails] = pydantic.Field()
    """
    A list of daily metrics, only days with ingested data are included.
    """

    meta: UtilsMetaResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
