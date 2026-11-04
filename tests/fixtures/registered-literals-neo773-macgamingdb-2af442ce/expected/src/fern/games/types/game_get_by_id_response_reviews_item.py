

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .game_get_by_id_response_reviews_item_chipset_variant import GameGetByIdResponseReviewsItemChipsetVariant
from .game_get_by_id_response_reviews_item_graphics_settings import GameGetByIdResponseReviewsItemGraphicsSettings
from .game_get_by_id_response_reviews_item_mac_config import GameGetByIdResponseReviewsItemMacConfig
from .game_get_by_id_response_reviews_item_performance import GameGetByIdResponseReviewsItemPerformance
from .game_get_by_id_response_reviews_item_play_method import GameGetByIdResponseReviewsItemPlayMethod
from .game_get_by_id_response_reviews_item_translation_layer import GameGetByIdResponseReviewsItemTranslationLayer


class GameGetByIdResponseReviewsItem(UniversalBaseModel):
    id: str
    game_id: typing_extensions.Annotated[str, FieldMetadata(alias="gameId"), pydantic.Field(alias="gameId")]
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    play_method: typing_extensions.Annotated[
        GameGetByIdResponseReviewsItemPlayMethod, FieldMetadata(alias="playMethod"), pydantic.Field(alias="playMethod")
    ]
    translation_layer: typing_extensions.Annotated[
        typing.Optional[GameGetByIdResponseReviewsItemTranslationLayer],
        FieldMetadata(alias="translationLayer"),
        pydantic.Field(alias="translationLayer"),
    ] = None
    performance: GameGetByIdResponseReviewsItemPerformance
    fps: typing.Optional[float] = None
    graphics_settings: typing_extensions.Annotated[
        typing.Optional[GameGetByIdResponseReviewsItemGraphicsSettings],
        FieldMetadata(alias="graphicsSettings"),
        pydantic.Field(alias="graphicsSettings"),
    ] = None
    resolution: typing.Optional[str] = None
    chipset: str
    chipset_variant: typing_extensions.Annotated[
        GameGetByIdResponseReviewsItemChipsetVariant,
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
        typing.Optional[GameGetByIdResponseReviewsItemMacConfig],
        FieldMetadata(alias="macConfig"),
        pydantic.Field(alias="macConfig"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
