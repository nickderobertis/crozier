

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from .tracing_type import TracingType


class TracingCapability(UniversalBaseModel):
    supported_scopes: typing.List[ApisV1ComponentsObservationScope]
    type: TracingType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
