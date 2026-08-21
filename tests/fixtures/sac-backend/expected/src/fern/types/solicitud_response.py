

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .canal_origen import CanalOrigen
from .estado_solicitud import EstadoSolicitud
from .prioridad import Prioridad
from .tipo_solicitud import TipoSolicitud


class SolicitudResponse(UniversalBaseModel):
    """
    Representación completa de una solicitud académica
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID único de la solicitud
    """

    solicitante_nombre: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="solicitanteNombre"),
        pydantic.Field(alias="solicitanteNombre", description="Nombre completo del solicitante"),
    ] = None
    """
    Nombre completo del solicitante
    """

    solicitante_correo: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="solicitanteCorreo"),
        pydantic.Field(alias="solicitanteCorreo", description="Correo electrónico del solicitante"),
    ] = None
    """
    Correo electrónico del solicitante
    """

    solicitante_telefono: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="solicitanteTelefono"),
        pydantic.Field(alias="solicitanteTelefono", description="Número de teléfono del solicitante"),
    ] = None
    """
    Número de teléfono del solicitante
    """

    solicitante_identificacion: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="solicitanteIdentificacion"),
        pydantic.Field(alias="solicitanteIdentificacion", description="Número de identificación del solicitante"),
    ] = None
    """
    Número de identificación del solicitante
    """

    asunto: typing.Optional[str] = pydantic.Field(default=None)
    """
    Asunto o título de la solicitud
    """

    descripcion: typing.Optional[str] = pydantic.Field(default=None)
    """
    Descripción detallada de la solicitud
    """

    canal_origen: typing_extensions.Annotated[
        typing.Optional[CanalOrigen], FieldMetadata(alias="canalOrigen"), pydantic.Field(alias="canalOrigen")
    ] = None
    fecha_hora_registro: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="fechaHoraRegistro"),
        pydantic.Field(alias="fechaHoraRegistro", description="Timestamp cuando fue registrada la solicitud"),
    ] = None
    """
    Timestamp cuando fue registrada la solicitud
    """

    tipo: typing.Optional[TipoSolicitud] = None
    prioridad: typing.Optional[Prioridad] = None
    nota_clasificacion: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="notaClasificacion"),
        pydantic.Field(alias="notaClasificacion", description="Nota de clasificación y justificación de la prioridad"),
    ] = None
    """
    Nota de clasificación y justificación de la prioridad
    """

    estado: typing.Optional[EstadoSolicitud] = None
    resolucion: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resolución de la solicitud (solo presente cuando estado es CERRADA)
    """

    notas_cierre: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="notasCierre"),
        pydantic.Field(
            alias="notasCierre", description="Notas adicionales del cierre (solo presente cuando estado es CERRADA)"
        ),
    ] = None
    """
    Notas adicionales del cierre (solo presente cuando estado es CERRADA)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
