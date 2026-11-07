

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    """
    Details of an API error.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short description of the error.
    """

    error_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Platform code for the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
