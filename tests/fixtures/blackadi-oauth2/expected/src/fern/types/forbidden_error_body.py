

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ForbiddenErrorBody(UniversalBaseModel):
    error: typing.Optional[str] = None
    error_description: typing.Optional[str] = None
    acr_values: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required ACR values for re-authorization.
    """

    max_age: typing.Optional[str] = pydantic.Field(default=None)
    """
    Maximum authentication age for re-authorization.
    """

    acr: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current ACR of the token.
    """

    auth_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    Current auth_time of the token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
