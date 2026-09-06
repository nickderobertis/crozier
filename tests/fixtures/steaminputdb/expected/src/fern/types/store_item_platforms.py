

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_platforms_vr_support import StoreItemPlatformsVrSupport


class StoreItemPlatforms(UniversalBaseModel):
    mac: typing.Optional[bool] = None
    steam_deck_compat_category: typing.Optional[int] = None
    steam_os_compat_category: typing.Optional[int] = None
    steamos_linux: typing.Optional[bool] = None
    vr_support: typing.Optional[StoreItemPlatformsVrSupport] = None
    windows: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
