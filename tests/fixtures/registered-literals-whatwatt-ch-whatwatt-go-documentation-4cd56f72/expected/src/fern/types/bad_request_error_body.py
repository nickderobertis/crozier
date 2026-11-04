

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBody(UniversalBaseModel):
    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short machine-readable error key
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
