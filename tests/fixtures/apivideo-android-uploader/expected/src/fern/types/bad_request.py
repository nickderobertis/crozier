

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .additional_bad_request_errors import AdditionalBadRequestErrors


class BadRequest(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the error documentation.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the error that occurred.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the parameter that caused the error.
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    The HTTP status code.
    """

    problems: typing.Optional[typing.List[AdditionalBadRequestErrors]] = pydantic.Field(default=None)
    """
    Returns any additional problems in the request in an array of objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
