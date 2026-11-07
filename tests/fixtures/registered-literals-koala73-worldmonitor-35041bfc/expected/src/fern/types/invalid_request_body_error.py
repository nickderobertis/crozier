

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvalidRequestBodyError(UniversalBaseModel):
    """
    Returned when a JSON POST request body is empty or malformed.
    """

    message: str = pydantic.Field()
    """
    Invalid request body
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
