

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_config_gear_asset_data_base_definition import DestinyConfigGearAssetDataBaseDefinition
from .destiny_config_image_pyramid_entry import DestinyConfigImagePyramidEntry


class DestinyConfigDestinyManifest(UniversalBaseModel):
    """
    DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.
    """

    icon_image_pyramid_info: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyConfigImagePyramidEntry]],
        FieldMetadata(alias="iconImagePyramidInfo"),
        pydantic.Field(
            alias="iconImagePyramidInfo",
            description='Information about the "Image Pyramid" for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the "original/full size" Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable)',
        ),
    ] = None
    """
    Information about the "Image Pyramid" for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the "original/full size" Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable)
    """

    json_world_component_content_paths: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="jsonWorldComponentContentPaths"),
        pydantic.Field(
            alias="jsonWorldComponentContentPaths",
            description="This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term.",
        ),
    ] = None
    """
    This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term.
    """

    json_world_content_paths: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="jsonWorldContentPaths"),
        pydantic.Field(
            alias="jsonWorldContentPaths",
            description="This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!)",
        ),
    ] = None
    """
    This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!)
    """

    mobile_asset_content_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mobileAssetContentPath"),
        pydantic.Field(alias="mobileAssetContentPath"),
    ] = None
    mobile_clan_banner_database_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mobileClanBannerDatabasePath"),
        pydantic.Field(alias="mobileClanBannerDatabasePath"),
    ] = None
    mobile_gear_asset_data_bases: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyConfigGearAssetDataBaseDefinition]],
        FieldMetadata(alias="mobileGearAssetDataBases"),
        pydantic.Field(alias="mobileGearAssetDataBases"),
    ] = None
    mobile_gear_cdn: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="mobileGearCDN"),
        pydantic.Field(alias="mobileGearCDN"),
    ] = None
    mobile_world_content_paths: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="mobileWorldContentPaths"),
        pydantic.Field(alias="mobileWorldContentPaths"),
    ] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
