

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_type import ErrorType


class Error(UniversalBaseModel):
    type: ErrorType
    code: str = pydantic.Field()
    """
    Implementation-defined error code
    """

    message: str
    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    RFC 9535 JSONPath (optional)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
