

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_any_and_unknown_response_result_data import ComplexTypesAnyAndUnknownResponseResultData


class ComplexTypesAnyAndUnknownResponseResult(UniversalBaseModel):
    data: ComplexTypesAnyAndUnknownResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
