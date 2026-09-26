

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_origin import ErrorOrigin


class Error(UniversalBaseModel):
    """
    RFC7807-compliant error description
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Summary of the problem
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP status code
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Explanation specific to this occurrence of the problem
    """

    origin: typing.Optional[ErrorOrigin] = pydantic.Field(default=None)
    """
    Origin of where the error was generated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
