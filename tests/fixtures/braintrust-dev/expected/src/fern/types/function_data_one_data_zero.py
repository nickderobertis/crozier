

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .code_bundle import CodeBundle
from .function_data_one_data_zero_type import FunctionDataOneDataZeroType


class FunctionDataOneDataZero(CodeBundle):
    type: FunctionDataOneDataZeroType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
