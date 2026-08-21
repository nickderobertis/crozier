

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HistorialResponse(UniversalBaseModel):
    """
    Entrada única del historial de auditoría para una solicitud
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID único de la entrada del historial
    """

    fecha_hora: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="fechaHora"),
        pydantic.Field(alias="fechaHora", description="Timestamp de la acción"),
    ] = None
    """
    Timestamp de la acción
    """

    accion: typing.Optional[str] = pydantic.Field(default=None)
    """
    Descripción de la acción realizada
    """

    usuario_responsable: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="usuarioResponsable"),
        pydantic.Field(alias="usuarioResponsable", description="Nombre de usuario que realizó la acción"),
    ] = None
    """
    Nombre de usuario que realizó la acción
    """

    observaciones: typing.Optional[str] = pydantic.Field(default=None)
    """
    Observaciones adicionales sobre la acción
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
