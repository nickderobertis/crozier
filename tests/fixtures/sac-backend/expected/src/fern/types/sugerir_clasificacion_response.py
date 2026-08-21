

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .prioridad import Prioridad
from .tipo_solicitud import TipoSolicitud


class SugerirClasificacionResponse(UniversalBaseModel):
    """
    Sugerencias de tipo y prioridad generadas por IA (RF-10).
    Estas sugerencias deben ser confirmadas o ajustadas por un usuario humano antes de aplicarse.
    """

    tipo_sugerido: typing_extensions.Annotated[
        typing.Optional[TipoSolicitud],
        FieldMetadata(alias="tipoSugerido"),
        pydantic.Field(alias="tipoSugerido", description="Tipo de solicitud sugerido por el modelo de lenguaje"),
    ] = None
    """
    Tipo de solicitud sugerido por el modelo de lenguaje
    """

    prioridad_sugerida: typing_extensions.Annotated[
        typing.Optional[Prioridad],
        FieldMetadata(alias="prioridadSugerida"),
        pydantic.Field(alias="prioridadSugerida", description="Prioridad sugerida por el modelo de lenguaje"),
    ] = None
    """
    Prioridad sugerida por el modelo de lenguaje
    """

    justificacion: typing.Optional[str] = pydantic.Field(default=None)
    """
    Explicación del razonamiento del modelo de lenguaje
    """

    confianza: typing.Optional[float] = pydantic.Field(default=None)
    """
    Nivel de confianza del modelo (0.0 – 1.0). Orientativo para el usuario.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
