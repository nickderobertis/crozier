

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rol_usuario import RolUsuario


class IniciarSesionResponse(UniversalBaseModel):
    """
    Respuesta de autenticación JWT
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token de acceso JWT
    """

    tipo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tipo de token
    """

    nombre_usuario: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nombreUsuario"),
        pydantic.Field(alias="nombreUsuario", description="Nombre de usuario autenticado"),
    ] = None
    """
    Nombre de usuario autenticado
    """

    rol: typing.Optional[RolUsuario] = None
    expira_en: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expiraEn"),
        pydantic.Field(alias="expiraEn", description="Tiempo de expiración del token en segundos"),
    ] = None
    """
    Tiempo de expiración del token en segundos
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
