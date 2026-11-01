

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inferred_returns_string_literal_response_result_data import InferredReturnsStringLiteralResponseResultData


class InferredReturnsStringLiteralResponseResult(UniversalBaseModel):
    data: InferredReturnsStringLiteralResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
