

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_nullish_one_data import FunctionDataNullishOneData
from .function_data_nullish_one_type import FunctionDataNullishOneType


class FunctionDataNullishOne(UniversalBaseModel):
    type: FunctionDataNullishOneType
    data: FunctionDataNullishOneData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
