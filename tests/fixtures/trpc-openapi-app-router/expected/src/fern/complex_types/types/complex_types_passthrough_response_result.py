

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_passthrough_response_result_data import ComplexTypesPassthroughResponseResultData


class ComplexTypesPassthroughResponseResult(UniversalBaseModel):
    data: ComplexTypesPassthroughResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
