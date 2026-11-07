

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Exception(UniversalBaseModel):
    """
    Exception object contains specific error code and its message related to the API request validation error or error occurred during API request processing.
    """

    code: str = pydantic.Field()
    """
    Indicates the type of error occured.
    """

    details: str = pydantic.Field()
    """
    Describes what went wrong.
    """

    message: str = pydantic.Field()
    """
    Indicates the error message that describes the error code.
    """

    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
