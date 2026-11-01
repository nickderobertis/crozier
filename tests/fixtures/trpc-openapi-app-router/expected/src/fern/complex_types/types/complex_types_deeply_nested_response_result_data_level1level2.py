

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_deeply_nested_response_result_data_level1level2level3 import (
    ComplexTypesDeeplyNestedResponseResultDataLevel1Level2Level3,
)


class ComplexTypesDeeplyNestedResponseResultDataLevel1Level2(UniversalBaseModel):
    level3: ComplexTypesDeeplyNestedResponseResultDataLevel1Level2Level3

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
