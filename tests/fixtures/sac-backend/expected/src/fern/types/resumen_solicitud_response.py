

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResumenSolicitudResponse(UniversalBaseModel):
    """
    Resumen textual de una solicitud generado por IA (RF-09)
    """

    id_solicitud: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="idSolicitud"),
        pydantic.Field(alias="idSolicitud", description="ID de la solicitud resumida"),
    ] = None
    """
    ID de la solicitud resumida
    """

    resumen: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resumen narrativo del estado e historial completo de la solicitud
    """

    generado_en: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="generadoEn"),
        pydantic.Field(alias="generadoEn", description="Marca de tiempo de cuando fue generado el resumen"),
    ] = None
    """
    Marca de tiempo de cuando fue generado el resumen
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
