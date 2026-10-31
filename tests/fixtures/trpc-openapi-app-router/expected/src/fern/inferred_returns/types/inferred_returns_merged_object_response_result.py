

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inferred_returns_merged_object_response_result_data import InferredReturnsMergedObjectResponseResultData


class InferredReturnsMergedObjectResponseResult(UniversalBaseModel):
    data: InferredReturnsMergedObjectResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
