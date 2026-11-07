

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_internal_server_error_issues_item import ErrorInternalServerErrorIssuesItem


class ErrorInternalServerError(UniversalBaseModel):
    """
    The error information
    """

    message: str = pydantic.Field()
    """
    The error message
    """

    code: str = pydantic.Field()
    """
    The error code
    """

    issues: typing.Optional[typing.List[ErrorInternalServerErrorIssuesItem]] = pydantic.Field(default=None)
    """
    An array of issues that were responsible for the error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
