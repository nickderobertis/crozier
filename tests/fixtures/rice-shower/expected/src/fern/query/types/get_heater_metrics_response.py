

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_heater_metrics_response_metrics_item import GetHeaterMetricsResponseMetricsItem


class GetHeaterMetricsResponse(UniversalBaseModel):
    data_points: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="dataPoints"),
        pydantic.Field(alias="dataPoints", description="Total number of data points returned"),
    ]
    """
    Total number of data points returned
    """

    metrics: typing.List[GetHeaterMetricsResponseMetricsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
