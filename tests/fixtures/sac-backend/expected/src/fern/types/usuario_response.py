

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rol_usuario import RolUsuario


class UsuarioResponse(UniversalBaseModel):
    """
    Información del usuario (la contraseña nunca se expone)
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID único del usuario
    """

    nombre_completo: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nombreCompleto"),
        pydantic.Field(alias="nombreCompleto", description="Nombre completo del usuario"),
    ] = None
    """
    Nombre completo del usuario
    """

    nombre_usuario: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nombreUsuario"),
        pydantic.Field(alias="nombreUsuario", description="Nombre de usuario"),
    ] = None
    """
    Nombre de usuario
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Correo electrónico del usuario
    """

    rol: typing.Optional[RolUsuario] = None
    activo: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Si la cuenta del usuario está activa
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
