

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_php_info_loaded_extensions_item import GetPhpInfoLoadedExtensionsItem


class GetPhpInfo(UniversalBaseModel):
    php_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="phpVersion"),
        pydantic.Field(alias="phpVersion", description="Version of PHP"),
    ] = None
    """
    Version of PHP
    """

    loaded_extensions: typing_extensions.Annotated[
        typing.Optional[typing.List[GetPhpInfoLoadedExtensionsItem]],
        FieldMetadata(alias="loadedExtensions"),
        pydantic.Field(alias="loadedExtensions", description="List of loaded extensions in PHP"),
    ] = None
    """
    List of loaded extensions in PHP
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
