

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RestApiResponseError(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error code
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional error details
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
