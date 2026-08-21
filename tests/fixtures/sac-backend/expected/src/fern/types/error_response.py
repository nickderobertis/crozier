

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    """
    Cuerpo de respuesta de error estándar
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp de ocurrencia del error
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    Código de estado HTTP
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Frase de razón del error HTTP
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Mensaje de error detallado
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ruta de solicitud que causó el error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
