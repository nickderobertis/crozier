

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreItemReleaseInfo(UniversalBaseModel):
    coming_soon_display: typing.Optional[str] = None
    custom_release_date_message: typing.Optional[str] = None
    is_abridged_release_date: typing.Optional[bool] = None
    is_coming_soon: typing.Optional[bool] = None
    is_early_access: typing.Optional[bool] = None
    is_preload: typing.Optional[bool] = None
    limited_launch_active: typing.Optional[bool] = None
    linux_release_date: typing.Optional[int] = None
    mac_release_date: typing.Optional[int] = None
    original_release_date: typing.Optional[int] = None
    original_steam_release_date: typing.Optional[int] = None
    steam_release_date: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
