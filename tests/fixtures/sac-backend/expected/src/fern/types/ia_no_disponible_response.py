

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IaNoDisponibleResponse(UniversalBaseModel):
    """
    Respuesta retornada cuando el servicio de IA externo no está disponible (RF-11).
    El resto del sistema continúa operando con normalidad; el usuario debe realizar
    la acción correspondiente de forma manual.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Momento en que se produjo el error
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    Código HTTP de la respuesta
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Descripción breve del error
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Mensaje de orientación para el usuario
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
