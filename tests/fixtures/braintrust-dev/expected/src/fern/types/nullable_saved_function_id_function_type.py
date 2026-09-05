

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_type_enum import FunctionTypeEnum
from .nullable_saved_function_id_function_type_type import NullableSavedFunctionIdFunctionTypeType


class NullableSavedFunctionIdFunctionType(UniversalBaseModel):
    type: NullableSavedFunctionIdFunctionTypeType
    name: str
    function_type: typing.Optional[FunctionTypeEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
