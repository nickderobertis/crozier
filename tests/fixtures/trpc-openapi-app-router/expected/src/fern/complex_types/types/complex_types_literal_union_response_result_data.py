

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_literal_union_response_result_data_color import ComplexTypesLiteralUnionResponseResultDataColor


class ComplexTypesLiteralUnionResponseResultData(UniversalBaseModel):
    color: ComplexTypesLiteralUnionResponseResultDataColor

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
