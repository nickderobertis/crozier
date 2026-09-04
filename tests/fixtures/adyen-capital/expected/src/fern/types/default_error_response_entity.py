

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .invalid_field import InvalidField


class DefaultErrorResponseEntity(UniversalBaseModel):
    """
    Standardized error response following RFC-7807 format
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable explanation specific to this occurrence of the problem.
    """

    error_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorCode"),
        pydantic.Field(alias="errorCode", description="Unique business error code."),
    ] = None
    """
    Unique business error code.
    """

    instance: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URI that identifies the specific occurrence of the problem if applicable.
    """

    invalid_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[InvalidField]],
        FieldMetadata(alias="invalidFields"),
        pydantic.Field(alias="invalidFields", description="Array of fields with validation errors when applicable."),
    ] = None
    """
    Array of fields with validation errors when applicable.
    """

    request_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="The unique reference for the request."),
    ] = None
    """
    The unique reference for the request.
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    The HTTP status code.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short, human-readable summary of the problem type.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URI that identifies the validation error type. It points to human-readable documentation for the problem type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
