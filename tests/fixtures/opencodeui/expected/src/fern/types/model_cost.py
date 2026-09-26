

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .model_cost_cache import ModelCostCache
from .model_cost_experimental_over200k import ModelCostExperimentalOver200K


class ModelCost(UniversalBaseModel):
    input: float
    output: float
    cache: ModelCostCache
    experimental_over200k: typing_extensions.Annotated[
        typing.Optional[ModelCostExperimentalOver200K],
        FieldMetadata(alias="experimentalOver200K"),
        pydantic.Field(alias="experimentalOver200K"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
