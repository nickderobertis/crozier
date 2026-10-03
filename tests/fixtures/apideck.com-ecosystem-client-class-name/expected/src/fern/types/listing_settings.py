

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .listing_settings_naming import ListingSettingsNaming
from .listing_settings_sidebar_position import ListingSettingsSidebarPosition


class ListingSettings(UniversalBaseModel):
    description_text_template: typing.Optional[str] = None
    description_title: typing.Optional[str] = None
    features_text_template: typing.Optional[str] = None
    features_title: typing.Optional[str] = None
    install_button_label: typing.Optional[str] = None
    name_postfix: typing.Optional[str] = None
    naming: typing.Optional[ListingSettingsNaming] = None
    native_integration_link: typing.Optional[str] = None
    pricing_disabled: typing.Optional[bool] = None
    pricing_text_template: typing.Optional[str] = None
    pricing_title: typing.Optional[str] = None
    sidebar_position: typing.Optional[ListingSettingsSidebarPosition] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
