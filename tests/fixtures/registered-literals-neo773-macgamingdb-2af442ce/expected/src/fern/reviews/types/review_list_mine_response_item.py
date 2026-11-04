

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .review_list_mine_response_item_chipset_variant import ReviewListMineResponseItemChipsetVariant
from .review_list_mine_response_item_graphics_settings import ReviewListMineResponseItemGraphicsSettings
from .review_list_mine_response_item_mac_config import ReviewListMineResponseItemMacConfig
from .review_list_mine_response_item_performance import ReviewListMineResponseItemPerformance
from .review_list_mine_response_item_play_method import ReviewListMineResponseItemPlayMethod
from .review_list_mine_response_item_translation_layer import ReviewListMineResponseItemTranslationLayer


class ReviewListMineResponseItem(UniversalBaseModel):
    id: str
    game_id: typing_extensions.Annotated[str, FieldMetadata(alias="gameId"), pydantic.Field(alias="gameId")]
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    play_method: typing_extensions.Annotated[
        ReviewListMineResponseItemPlayMethod, FieldMetadata(alias="playMethod"), pydantic.Field(alias="playMethod")
    ]
    translation_layer: typing_extensions.Annotated[
        typing.Optional[ReviewListMineResponseItemTranslationLayer],
        FieldMetadata(alias="translationLayer"),
        pydantic.Field(alias="translationLayer"),
    ] = None
    performance: ReviewListMineResponseItemPerformance
    fps: typing.Optional[float] = None
    graphics_settings: typing_extensions.Annotated[
        typing.Optional[ReviewListMineResponseItemGraphicsSettings],
        FieldMetadata(alias="graphicsSettings"),
        pydantic.Field(alias="graphicsSettings"),
    ] = None
    resolution: typing.Optional[str] = None
    chipset: str
    chipset_variant: typing_extensions.Annotated[
        ReviewListMineResponseItemChipsetVariant,
        FieldMetadata(alias="chipsetVariant"),
        pydantic.Field(alias="chipsetVariant"),
    ]
    mac_config_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="macConfigId"), pydantic.Field(alias="macConfigId")
    ] = None
    notes: typing.Optional[str] = None
    screenshots: typing.Optional[str] = None
    software_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="softwareVersion"), pydantic.Field(alias="softwareVersion")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    mac_config: typing_extensions.Annotated[
        typing.Optional[ReviewListMineResponseItemMacConfig],
        FieldMetadata(alias="macConfig"),
        pydantic.Field(alias="macConfig"),
    ] = None
    game_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="gameName"), pydantic.Field(alias="gameName")
    ] = None
    game_slug: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="gameSlug"), pydantic.Field(alias="gameSlug")
    ] = None
    game_header_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="gameHeaderImage"), pydantic.Field(alias="gameHeaderImage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
