

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_defined_error_error_type import UserDefinedErrorErrorType


class UserDefinedError(UniversalBaseModel):
    error_code: str
    reasoning: str
    confidence_float: float
    error_type: typing.Optional[UserDefinedErrorErrorType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
