

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .metric_observation_inputs_item_value import MetricObservationInputsItemValue


class MetricObservationInputsItem(UniversalBaseModel):
    name: str
    value: typing.Optional[MetricObservationInputsItemValue] = None
    as_of: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="asOf"), pydantic.Field(alias="asOf")
    ] = None
    observation: "MetricObservation"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .metric_observation import MetricObservation

update_forward_refs(MetricObservationInputsItem, MetricObservation=MetricObservation)
