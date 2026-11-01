

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_details import ErrorDetails


class ServiceUnavailableErrorBody(UniversalBaseModel):
    """
    The JSON body that LoonFS APIs return with an HTTP error status.
    """

    code: str = pydantic.Field()
    """
    The stable, machine-readable error code.
    """

    details: typing.Optional[ErrorDetails] = pydantic.Field(default=None)
    """
    Optional machine-readable context for the error code.
    """

    feature: typing.Optional[str] = pydantic.Field(default=None)
    """
    The capability feature that isn't supported, when the code is `not_supported`.
    """

    message: str = pydantic.Field()
    """
    A human-readable description of the error.
    """

    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    The invalid input, as a JSON Pointer, a parameter name, a CLI flag, or a CLI argument.
    """

    request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The request ID. The server also sends this ID in the `x-request-id` response header.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
