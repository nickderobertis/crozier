

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModuleFederationDto(UniversalBaseModel):
    """
    Module federation
    """

    exposed_module: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="exposedModule"),
        pydantic.Field(alias="exposedModule", description="Module name see exposes in webpack.config.js"),
    ] = None
    """
    Module name see exposes in webpack.config.js
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name"),
    ] = None
    """
    Display name
    """

    route_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="routePath"), pydantic.Field(alias="routePath", description="Route")
    ] = None
    """
    Route
    """

    ng_module_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ngModuleName"),
        pydantic.Field(alias="ngModuleName", description="NgModuleName"),
    ] = None
    """
    NgModuleName
    """

    source_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourcePath"),
        pydantic.Field(alias="sourcePath", description="Need for module federation export"),
    ] = None
    """
    Need for module federation export
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
