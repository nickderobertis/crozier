

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_complex_arrays_response_result import ComplexTypesComplexArraysResponseResult


class ComplexTypesComplexArraysResponse(UniversalBaseModel):
    result: ComplexTypesComplexArraysResponseResult

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
