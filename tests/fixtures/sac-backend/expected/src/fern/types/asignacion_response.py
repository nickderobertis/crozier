

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AsignacionResponse(UniversalBaseModel):
    """
    Representación de una asignación solicitud-a-usuario
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID único de la asignación
    """

    solicitud_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="solicitudId"),
        pydantic.Field(alias="solicitudId", description="ID de la solicitud asignada"),
    ] = None
    """
    ID de la solicitud asignada
    """

    usuario_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="usuarioId"),
        pydantic.Field(alias="usuarioId", description="ID del usuario asignado"),
    ] = None
    """
    ID del usuario asignado
    """

    fecha_asignacion: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="fechaAsignacion"),
        pydantic.Field(alias="fechaAsignacion", description="Timestamp de la asignación"),
    ] = None
    """
    Timestamp de la asignación
    """

    activa: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Si esta asignación está actualmente activa
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
