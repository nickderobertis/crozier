

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestException(UniversalBaseModel):
    """
    An exception object returned when a request fails.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A text description associated with the BadRequestException object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
