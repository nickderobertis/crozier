

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trend import Trend


class TestConformanceMetric(UniversalBaseModel):
    """
    Represents the test conformance metrics (current score, history and evolution trend) of a Service
    """

    aggregation_label_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="aggregationLabelValue"),
        pydantic.Field(
            alias="aggregationLabelValue", description="Value of the label used for metrics aggregation (if any)"
        ),
    ] = None
    """
    Value of the label used for metrics aggregation (if any)
    """

    current_score: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="currentScore"),
        pydantic.Field(alias="currentScore", description="Current test conformance score for the related Service"),
    ]
    """
    Current test conformance score for the related Service
    """

    id: str = pydantic.Field()
    """
    Unique identifier of coverage metric
    """

    last_update_day: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdateDay"),
        pydantic.Field(alias="lastUpdateDay", description="The day of latest score update (in yyyyMMdd format)"),
    ] = None
    """
    The day of latest score update (in yyyyMMdd format)
    """

    latest_scores: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, float]],
        FieldMetadata(alias="latestScores"),
        pydantic.Field(
            alias="latestScores",
            description="History of latest scores (key is date with format yyyyMMdd, value is score as double)",
        ),
    ] = None
    """
    History of latest scores (key is date with format yyyyMMdd, value is score as double)
    """

    latest_trend: typing_extensions.Annotated[
        typing.Optional[Trend],
        FieldMetadata(alias="latestTrend"),
        pydantic.Field(alias="latestTrend", description="Evolution trend of currentScore"),
    ] = None
    """
    Evolution trend of currentScore
    """

    max_possible_score: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maxPossibleScore"),
        pydantic.Field(
            alias="maxPossibleScore",
            description="Maximum conformance score that can be reached (depends on samples expresiveness)",
        ),
    ]
    """
    Maximum conformance score that can be reached (depends on samples expresiveness)
    """

    service_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceId"),
        pydantic.Field(alias="serviceId", description="Unique identifier of the Service this metric is related to"),
    ]
    """
    Unique identifier of the Service this metric is related to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
