

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inferred_returns_primitive_union_response_result_data_value import (
    InferredReturnsPrimitiveUnionResponseResultDataValue,
)


class InferredReturnsPrimitiveUnionResponseResultData(UniversalBaseModel):
    value: InferredReturnsPrimitiveUnionResponseResultDataValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
