

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marketplace_id import MarketplaceId
from .metric_observation_currency import MetricObservationCurrency
from .metric_observation_provenance import MetricObservationProvenance
from .metric_observation_quality import MetricObservationQuality
from .metric_observation_time_grain import MetricObservationTimeGrain
from .metric_observation_unit import MetricObservationUnit


class MetricObservation(UniversalBaseModel):
    id: str
    tenant_id: str
    materialization_id: str
    evidence_import_id: str
    platform: MarketplaceId
    metric_key: str
    value_decimal: str = pydantic.Field()
    """
    Exact finite base-10 value serialized as a string; at most 38 significant digits and scale 9. NaN, infinity, exponent notation, and overflow are rejected.
    """

    unit: MetricObservationUnit
    currency: typing.Optional[MetricObservationCurrency] = pydantic.Field(default=None)
    """
    Required for unit=currency and null for non-monetary observations. Missing monetary currency is quarantined instead of inferred.
    """

    period_start: dt.datetime
    period_end: dt.datetime
    time_grain: MetricObservationTimeGrain = pydantic.Field()
    """
    snapshot is a point-in-time balance, day is one calendar day, and range uses the explicit period_start/period_end interval.
    """

    dimensions: typing.Dict[str, str]
    provenance: MetricObservationProvenance
    quality: MetricObservationQuality
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
