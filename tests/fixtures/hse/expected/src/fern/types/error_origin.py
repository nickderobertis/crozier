

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorOrigin(UniversalBaseModel):
    """
    Origin of where the error was generated
    """

    file: typing.Optional[str] = pydantic.Field(default=None)
    """
    File where the error was generated
    """

    lineno: typing.Optional[int] = pydantic.Field(default=None)
    """
    Line number where the error was generated
    """

    errno: typing.Optional[int] = pydantic.Field(default=None)
    """
    Errno value describing the error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
