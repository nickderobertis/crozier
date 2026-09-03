

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .method_not_allowed_error_body_error import MethodNotAllowedErrorBodyError


class MethodNotAllowedErrorBody(UniversalBaseModel):
    error: MethodNotAllowedErrorBodyError = pydantic.Field()
    """
    Error code, available in error response.
    """

    error_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error description, available in error response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
