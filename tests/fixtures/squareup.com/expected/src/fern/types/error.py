

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    """
    Represents an error encountered during a request to the Connect API.

    See [Handling errors](https://developer.squareup.com/docs/build-basics/handling-errors) for more information.
    """

    category: str = pydantic.Field()
    """
    The high-level category for the error.
    """

    code: str = pydantic.Field()
    """
    The specific code of the error.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable description of the error for debugging purposes.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the field provided in the original request (if any) that
    the error pertains to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
