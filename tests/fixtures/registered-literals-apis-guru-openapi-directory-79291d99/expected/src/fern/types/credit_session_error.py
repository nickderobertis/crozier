

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreditSessionError(UniversalBaseModel):
    """
    The details of a Link error.
    """

    display_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A user-friendly representation of the error code. `null` if the error is not related to user action.
    """

    error_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The particular error code.
    """

    error_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A developer-friendly representation of the error code.
    """

    error_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A broad categorization of the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
