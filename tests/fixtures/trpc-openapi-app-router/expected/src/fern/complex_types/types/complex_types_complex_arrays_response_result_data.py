

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .complex_types_complex_arrays_response_result_data_items_item import (
    ComplexTypesComplexArraysResponseResultDataItemsItem,
)


class ComplexTypesComplexArraysResponseResultData(UniversalBaseModel):
    tags: typing.List[str]
    items: typing.List[ComplexTypesComplexArraysResponseResultDataItemsItem]
    matrix: typing.List[typing.List[float]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
