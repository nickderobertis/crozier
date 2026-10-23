

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...core.serialization import FieldMetadata


class GetTokensAddressResponseReadingVolumeUsd24H(UniversalBaseModel):
    value: typing.Optional[float] = None
    source: typing.Optional[str] = None
    as_of: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="asOf"),
        pydantic.Field(
            alias="asOf",
            description="Compatibility observation time. Derived capitalization uses the oldest required input time; inspect observation.inputs for each input.",
        ),
    ] = None
    """
    Compatibility observation time. Derived capitalization uses the oldest required input time; inspect observation.inputs for each input.
    """

    reason: typing.Optional[str] = None
    observation: "MetricObservation"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from ...types.metric_observation import MetricObservation
from ...types.metric_observation_inputs_item import MetricObservationInputsItem

update_forward_refs(
    GetTokensAddressResponseReadingVolumeUsd24H,
    MetricObservation=MetricObservation,
    MetricObservationInputsItem=MetricObservationInputsItem,
)
