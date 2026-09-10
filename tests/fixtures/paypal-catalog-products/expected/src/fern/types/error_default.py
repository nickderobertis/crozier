

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error400message import Error400Message
from .error401message import Error401Message
from .error403message import Error403Message
from .error404message import Error404Message
from .error409message import Error409Message
from .error415message import Error415Message
from .error422message import Error422Message
from .error500message import Error500Message
from .error503message import Error503Message
from .error_details import ErrorDetails
from .error_link_description import ErrorLinkDescription


class ErrorDefault_InvalidRequest(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["INVALID_REQUEST"] = "INVALID_REQUEST"
    message: typing.Optional[Error400Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_AuthenticationFailure(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["AUTHENTICATION_FAILURE"] = "AUTHENTICATION_FAILURE"
    message: typing.Optional[Error401Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_NotAuthorized(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["NOT_AUTHORIZED"] = "NOT_AUTHORIZED"
    message: typing.Optional[Error403Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_ResourceNotFound(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["RESOURCE_NOT_FOUND"] = "RESOURCE_NOT_FOUND"
    message: typing.Optional[Error404Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_ResourceConflict(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["RESOURCE_CONFLICT"] = "RESOURCE_CONFLICT"
    message: typing.Optional[Error409Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_UnsupportedMediaType(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["UNSUPPORTED_MEDIA_TYPE"] = "UNSUPPORTED_MEDIA_TYPE"
    message: typing.Optional[Error415Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_UnprocessableEntity(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["UNPROCESSABLE_ENTITY"] = "UNPROCESSABLE_ENTITY"
    message: typing.Optional[Error422Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_InternalServerError(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["INTERNAL_SERVER_ERROR"] = "INTERNAL_SERVER_ERROR"
    message: typing.Optional[Error500Message] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ErrorDefault_ServiceUnavailable(UniversalBaseModel):
    """
    The default error response.
    """

    name: typing.Literal["SERVICE_UNAVAILABLE"] = "SERVICE_UNAVAILABLE"
    message: typing.Optional[Error503Message] = None
    debug_id: typing.Optional[str] = None
    links: typing.Optional[typing.List[ErrorLinkDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ErrorDefault = typing_extensions.Annotated[
    typing.Union[
        ErrorDefault_InvalidRequest,
        ErrorDefault_AuthenticationFailure,
        ErrorDefault_NotAuthorized,
        ErrorDefault_ResourceNotFound,
        ErrorDefault_ResourceConflict,
        ErrorDefault_UnsupportedMediaType,
        ErrorDefault_UnprocessableEntity,
        ErrorDefault_InternalServerError,
        ErrorDefault_ServiceUnavailable,
    ],
    pydantic.Field(discriminator="name"),
]
