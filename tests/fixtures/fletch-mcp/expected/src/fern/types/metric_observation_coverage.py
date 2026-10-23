

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metric_observation_coverage_status import MetricObservationCoverageStatus


class MetricObservationCoverage(UniversalBaseModel):
    status: MetricObservationCoverageStatus
    scope: str
    window_start_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="windowStartAt"), pydantic.Field(alias="windowStartAt")
    ] = None
    window_end_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="windowEndAt"), pydantic.Field(alias="windowEndAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
