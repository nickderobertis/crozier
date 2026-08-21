

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .solicitud_response import SolicitudResponse


class SolicitudesPaginadasResponse(UniversalBaseModel):
    """
    Wrapper de respuesta paginada para solicitudes
    """

    content: typing.Optional[typing.List[SolicitudResponse]] = None
    pagina: typing.Optional[int] = pydantic.Field(default=None)
    """
    Número de página actual (basado en cero)
    """

    tama_o: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="tamaño"),
        pydantic.Field(alias="tamaño", description="Número de elementos por página"),
    ] = None
    """
    Número de elementos por página
    """

    total_elementos: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalElementos"),
        pydantic.Field(alias="totalElementos", description="Número total de registros que coinciden"),
    ] = None
    """
    Número total de registros que coinciden
    """

    total_paginas: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalPaginas"),
        pydantic.Field(alias="totalPaginas", description="Número total de páginas"),
    ] = None
    """
    Número total de páginas
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
