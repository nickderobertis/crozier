

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_one_data import FunctionDataOneData
from .function_data_one_type import FunctionDataOneType


class FunctionDataOne(UniversalBaseModel):
    type: FunctionDataOneType
    data: FunctionDataOneData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
