

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_defaults_response_result_data_sort import ComplexTypesDefaultsResponseResultDataSort


class ComplexTypesDefaultsResponseResultData(UniversalBaseModel):
    page: float
    limit: float
    sort: ComplexTypesDefaultsResponseResultDataSort

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
