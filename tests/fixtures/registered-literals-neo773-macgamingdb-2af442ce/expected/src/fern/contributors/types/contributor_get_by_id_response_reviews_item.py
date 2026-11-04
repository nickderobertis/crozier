

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .contributor_get_by_id_response_reviews_item_chipset_variant import (
    ContributorGetByIdResponseReviewsItemChipsetVariant,
)
from .contributor_get_by_id_response_reviews_item_graphics_settings import (
    ContributorGetByIdResponseReviewsItemGraphicsSettings,
)
from .contributor_get_by_id_response_reviews_item_mac_config import ContributorGetByIdResponseReviewsItemMacConfig
from .contributor_get_by_id_response_reviews_item_performance import ContributorGetByIdResponseReviewsItemPerformance
from .contributor_get_by_id_response_reviews_item_play_method import ContributorGetByIdResponseReviewsItemPlayMethod
from .contributor_get_by_id_response_reviews_item_translation_layer import (
    ContributorGetByIdResponseReviewsItemTranslationLayer,
)


class ContributorGetByIdResponseReviewsItem(UniversalBaseModel):
    id: str
    game_id: typing_extensions.Annotated[str, FieldMetadata(alias="gameId"), pydantic.Field(alias="gameId")]
    game_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="gameName"), pydantic.Field(alias="gameName")
    ] = None
    game_slug: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="gameSlug"), pydantic.Field(alias="gameSlug")
    ] = None
    game_header_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="gameHeaderImage"), pydantic.Field(alias="gameHeaderImage")
    ] = None
    play_method: typing_extensions.Annotated[
        ContributorGetByIdResponseReviewsItemPlayMethod,
        FieldMetadata(alias="playMethod"),
        pydantic.Field(alias="playMethod"),
    ]
    software_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="softwareVersion"), pydantic.Field(alias="softwareVersion")
    ] = None
    translation_layer: typing_extensions.Annotated[
        typing.Optional[ContributorGetByIdResponseReviewsItemTranslationLayer],
        FieldMetadata(alias="translationLayer"),
        pydantic.Field(alias="translationLayer"),
    ] = None
    performance: ContributorGetByIdResponseReviewsItemPerformance
    fps: typing.Optional[float] = None
    chipset: str
    chipset_variant: typing_extensions.Annotated[
        ContributorGetByIdResponseReviewsItemChipsetVariant,
        FieldMetadata(alias="chipsetVariant"),
        pydantic.Field(alias="chipsetVariant"),
    ]
    graphics_settings: typing_extensions.Annotated[
        typing.Optional[ContributorGetByIdResponseReviewsItemGraphicsSettings],
        FieldMetadata(alias="graphicsSettings"),
        pydantic.Field(alias="graphicsSettings"),
    ] = None
    resolution: typing.Optional[str] = None
    notes: typing.Optional[str] = None
    screenshots: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    mac_config: typing_extensions.Annotated[
        typing.Optional[ContributorGetByIdResponseReviewsItemMacConfig],
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
