

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_info_item_type import AppInfoItemType
from .apps_platforms import AppsPlatforms
from .apps_release import AppsRelease
from .controller_support import ControllerSupport
from .store_item_assets import StoreItemAssets
from .store_item_basic_info import StoreItemBasicInfo


class AppInfoItem(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="$schema"),
        pydantic.Field(alias="$schema", description="A URL to the JSON Schema for this object."),
    ] = None
    """
    A URL to the JSON Schema for this object.
    """

    app_id: typing.Optional[int] = None
    assets: typing.Optional[StoreItemAssets] = None
    basic_info: typing.Optional[StoreItemBasicInfo] = None
    controller_support: typing.Optional[ControllerSupport] = None
    links: typing.Optional[typing.List[str]] = None
    name: typing.Optional[str] = None
    official_configs: typing.Optional[typing.Dict[str, int]] = None
    platforms: typing.Optional[AppsPlatforms] = None
    release: typing.Optional[AppsRelease] = None
    store_url_path: typing.Optional[str] = None
    type: AppInfoItemType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
