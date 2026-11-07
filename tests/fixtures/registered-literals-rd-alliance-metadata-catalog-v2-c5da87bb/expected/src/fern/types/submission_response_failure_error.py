

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .submission_response_failure_error_errors_item import SubmissionResponseFailureErrorErrorsItem


class SubmissionResponseFailureError(UniversalBaseModel):
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Summary of the error(s).
    """

    errors: typing.Optional[typing.List[SubmissionResponseFailureErrorErrorsItem]] = pydantic.Field(default=None)
    """
    Errors returned by form validation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
