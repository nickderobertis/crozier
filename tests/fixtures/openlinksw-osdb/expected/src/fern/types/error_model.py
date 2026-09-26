

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_model_status import ErrorModelStatus


class ErrorModel(UniversalBaseModel):
    api: typing.Optional[str] = pydantic.Field(default=None)
    """
    The path of the REST API method reporting the error
    """

    method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the REST API method reporting the error
    """

    response: typing.Optional[str] = pydantic.Field(default=None)
    """
    A message describing the error
    """

    status: typing.Optional[ErrorModelStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
