

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .global_config_response_observability_tianji import GlobalConfigResponseObservabilityTianji


class GlobalConfigResponseObservability(UniversalBaseModel):
    tianji: GlobalConfigResponseObservabilityTianji

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
