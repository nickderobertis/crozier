

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from .profiling_language import ProfilingLanguage
from .profiling_mode import ProfilingMode
from .profiling_type import ProfilingType


class ProfilingCapability(UniversalBaseModel):
    language: ProfilingLanguage
    modes: typing.List[ProfilingMode]
    supported_scopes: typing.List[ApisV1ComponentsObservationScope]
    supports_binary_match: bool
    type: ProfilingType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
