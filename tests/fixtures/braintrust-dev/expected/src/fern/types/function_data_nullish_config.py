

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_nullish_config_type import FunctionDataNullishConfigType
from .function_type_enum import FunctionTypeEnum


class FunctionDataNullishConfig(UniversalBaseModel):
    type: FunctionDataNullishConfigType
    name: str
    function_type: typing.Optional[FunctionTypeEnum] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Configuration options to pass to the global function (e.g., for preprocessor customization)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
