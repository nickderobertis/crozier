

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .theming_theming_get_manifest200response_icons_inner import ThemingThemingGetManifest200ResponseIconsInner


class ThemingThemingGetManifest200Response(UniversalBaseModel):
    name: str
    short_name: str
    start_url: str
    theme_color: str
    background_color: str
    description: str
    icons: typing.List[ThemingThemingGetManifest200ResponseIconsInner]
    display: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
