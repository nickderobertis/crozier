

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_nullish_one_data_code_runtime_context import FunctionDataNullishOneDataCodeRuntimeContext
from .function_data_nullish_one_data_code_type import FunctionDataNullishOneDataCodeType


class FunctionDataNullishOneDataCode(UniversalBaseModel):
    type: FunctionDataNullishOneDataCodeType
    runtime_context: FunctionDataNullishOneDataCodeRuntimeContext
    code: str
    code_hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA256 hash of the code, computed at save time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
