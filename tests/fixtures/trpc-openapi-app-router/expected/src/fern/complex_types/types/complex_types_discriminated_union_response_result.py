

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_discriminated_union_response_result_data import ComplexTypesDiscriminatedUnionResponseResultData


class ComplexTypesDiscriminatedUnionResponseResult(UniversalBaseModel):
    data: ComplexTypesDiscriminatedUnionResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
