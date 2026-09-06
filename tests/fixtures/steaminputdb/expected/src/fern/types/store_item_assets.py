

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StoreItemAssets(UniversalBaseModel):
    asset_url_format: typing.Optional[str] = None
    clan_avatar: typing.Optional[str] = None
    community_icon: typing.Optional[str] = None
    header: typing.Optional[str] = None
    hero_capsule: typing.Optional[str] = None
    hero_capsule2x: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hero_capsule_2x"), pydantic.Field(alias="hero_capsule_2x")
    ] = None
    library_capsule: typing.Optional[str] = None
    library_capsule2x: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="library_capsule_2x"), pydantic.Field(alias="library_capsule_2x")
    ] = None
    library_hero: typing.Optional[str] = None
    library_hero2x: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="library_hero_2x"), pydantic.Field(alias="library_hero_2x")
    ] = None
    main_capsule: typing.Optional[str] = None
    package_header: typing.Optional[str] = None
    page_background: typing.Optional[str] = None
    page_background_path: typing.Optional[str] = None
    raw_page_background: typing.Optional[str] = None
    small_capsule: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
