

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    code: int = pydantic.Field()
    """
    The HTTP error code associated with the error.
    """

    debug: typing.Optional[str] = None
    details: typing.Optional[typing.Dict[str, typing.Any]] = None
    err: str = pydantic.Field()
    """
    Human readable error message.
    """

    request: typing.Optional[str] = None
    status: str = pydantic.Field()
    """
    Machine readable representation of the HTTP error code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
