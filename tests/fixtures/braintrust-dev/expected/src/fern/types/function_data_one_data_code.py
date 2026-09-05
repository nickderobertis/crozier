

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_one_data_code_runtime_context import FunctionDataOneDataCodeRuntimeContext
from .function_data_one_data_code_type import FunctionDataOneDataCodeType


class FunctionDataOneDataCode(UniversalBaseModel):
    type: FunctionDataOneDataCodeType
    runtime_context: FunctionDataOneDataCodeRuntimeContext
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
