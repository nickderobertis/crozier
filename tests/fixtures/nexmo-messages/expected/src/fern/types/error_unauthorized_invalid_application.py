

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorUnauthorizedInvalidApplication(UniversalBaseModel):
    """
    Invalid Application Type
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional information about the error
    """

    instance: str = pydantic.Field()
    """
    Internal Trace ID
    """

    title: str = pydantic.Field()
    """
    Generic error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
