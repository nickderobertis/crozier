

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TooManyRequests(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the error documentation.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the error that occurred.
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    The HTTP status code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
