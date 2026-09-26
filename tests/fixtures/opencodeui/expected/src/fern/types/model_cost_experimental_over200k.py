

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_cost_experimental_over200k_cache import ModelCostExperimentalOver200KCache


class ModelCostExperimentalOver200K(UniversalBaseModel):
    input: float
    output: float
    cache: ModelCostExperimentalOver200KCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
