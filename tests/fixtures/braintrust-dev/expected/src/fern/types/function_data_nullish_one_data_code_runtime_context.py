

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_nullish_one_data_code_runtime_context_runtime import (
    FunctionDataNullishOneDataCodeRuntimeContextRuntime,
)


class FunctionDataNullishOneDataCodeRuntimeContext(UniversalBaseModel):
    runtime: FunctionDataNullishOneDataCodeRuntimeContextRuntime
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
