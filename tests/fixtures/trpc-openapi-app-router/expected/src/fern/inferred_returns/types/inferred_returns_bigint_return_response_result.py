

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inferred_returns_bigint_return_response_result_data import InferredReturnsBigintReturnResponseResultData


class InferredReturnsBigintReturnResponseResult(UniversalBaseModel):
    data: InferredReturnsBigintReturnResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
