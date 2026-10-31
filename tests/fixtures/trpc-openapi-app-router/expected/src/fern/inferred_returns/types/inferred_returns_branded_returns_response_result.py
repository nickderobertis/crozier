

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inferred_returns_branded_returns_response_result_data import InferredReturnsBrandedReturnsResponseResultData


class InferredReturnsBrandedReturnsResponseResult(UniversalBaseModel):
    data: InferredReturnsBrandedReturnsResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
