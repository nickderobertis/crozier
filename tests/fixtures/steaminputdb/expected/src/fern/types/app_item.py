

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_item_type import AppItemType
from .apps_platforms import AppsPlatforms
from .apps_release import AppsRelease
from .store_item_assets import StoreItemAssets
from .store_item_basic_info import StoreItemBasicInfo


class AppItem(UniversalBaseModel):
    app_id: typing.Optional[int] = None
    assets: typing.Optional[StoreItemAssets] = None
    basic_info: typing.Optional[StoreItemBasicInfo] = None
    links: typing.Optional[typing.List[str]] = None
    name: typing.Optional[str] = None
    platforms: typing.Optional[AppsPlatforms] = None
    release: typing.Optional[AppsRelease] = None
    store_url_path: typing.Optional[str] = None
    type: AppItemType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
