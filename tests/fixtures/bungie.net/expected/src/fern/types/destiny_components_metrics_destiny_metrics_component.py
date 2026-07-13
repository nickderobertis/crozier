

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_metrics_destiny_metric_component import DestinyComponentsMetricsDestinyMetricComponent


class DestinyComponentsMetricsDestinyMetricsComponent(UniversalBaseModel):
    metrics: typing.Optional[typing.Dict[str, DestinyComponentsMetricsDestinyMetricComponent]] = None
    metrics_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="metricsRootNodeHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
