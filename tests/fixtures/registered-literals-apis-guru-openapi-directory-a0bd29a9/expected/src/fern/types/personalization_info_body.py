

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PersonalizationInfoBody(UniversalBaseModel):
    dotfiles_install_command: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dotfilesInstallCommand"),
        pydantic.Field(alias="dotfilesInstallCommand"),
    ] = None
    dotfiles_repository: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dotfilesRepository"), pydantic.Field(alias="dotfilesRepository")
    ] = None
    dotfiles_target_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dotfilesTargetPath"), pydantic.Field(alias="dotfilesTargetPath")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
