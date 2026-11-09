

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NotFoundErrorBody(UniversalBaseModel):
    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    The HTTP status code of the error. Useful when passing the response
    body to child properties in a frontend UI. Must be returned as an integer.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short, human-readable summary of the problem. It should not
    change between occurences of a problem, except for localization.
    Should be provided as "Sentence case" for direct use in the UI.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error type.
    """

    instance: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used to return the correlation ID back to the user, in the format
    kong:trace:<correlation_id>. This helps us find the relevant logs
    when a customer reports an issue.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human readable explanation specific to this occurence of the problem.
    This field may contain request/entity data to help the user understand
    what went wrong. Enclose variable values in square brackets. Should be
    provided as "Sentence case" for direct use in the UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
