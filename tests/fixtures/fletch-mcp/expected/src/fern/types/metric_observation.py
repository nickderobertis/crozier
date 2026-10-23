

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .metric_observation_coverage import MetricObservationCoverage
from .metric_observation_parameters_value import MetricObservationParametersValue
from .metric_observation_read_status import MetricObservationReadStatus
from .metric_observation_status import MetricObservationStatus


class MetricObservation(UniversalBaseModel):
    source_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceId"),
        pydantic.Field(
            alias="sourceId",
            description="Stable source kind and identity; null when the stored source has no structured identity.",
        ),
    ] = None
    """
    Stable source kind and identity; null when the stored source has no structured identity.
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blockNumber"), pydantic.Field(alias="blockNumber")
    ] = None
    block_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blockHash"), pydantic.Field(alias="blockHash")
    ] = None
    source_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="sourceAt"),
        pydantic.Field(
            alias="sourceAt",
            description="Source moment, usually the pinned block timestamp. Unknown for explorer snapshots.",
        ),
    ] = None
    """
    Source moment, usually the pinned block timestamp. Unknown for explorer snapshots.
    """

    fetched_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="fetchedAt"),
        pydantic.Field(
            alias="fetchedAt",
            description="Recorded fetch/publication time. Null when older observations did not record it separately.",
        ),
    ] = None
    """
    Recorded fetch/publication time. Null when older observations did not record it separately.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="Inclusive hard freshness boundary. A derived value expires with its earliest-expiring required input.",
        ),
    ] = None
    """
    Inclusive hard freshness boundary. A derived value expires with its earliest-expiring required input.
    """

    method: str
    parameters: typing.Dict[str, typing.Optional[MetricObservationParametersValue]] = pydantic.Field()
    """
    Structured computation parameters, including historical quote sampling/oracle times and valuation assumptions when recorded.
    """

    inputs: typing.List["MetricObservationInputsItem"]
    coverage: MetricObservationCoverage
    status: MetricObservationStatus = pydantic.Field()
    """
    Timestamp validity and freshness, separate from read success and coverage.
    """

    read_status: typing_extensions.Annotated[
        MetricObservationReadStatus,
        FieldMetadata(alias="readStatus"),
        pydantic.Field(
            alias="readStatus", description="A retained current observation may coexist with a failed latest refresh."
        ),
    ]
    """
    A retained current observation may coexist with a failed latest refresh.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .metric_observation_inputs_item import MetricObservationInputsItem

update_forward_refs(MetricObservation, MetricObservationInputsItem=MetricObservationInputsItem)
