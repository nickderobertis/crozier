

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .review_create_response_review_chipset_variant import ReviewCreateResponseReviewChipsetVariant
from .review_create_response_review_graphics_settings import ReviewCreateResponseReviewGraphicsSettings
from .review_create_response_review_performance import ReviewCreateResponseReviewPerformance
from .review_create_response_review_play_method import ReviewCreateResponseReviewPlayMethod
from .review_create_response_review_translation_layer import ReviewCreateResponseReviewTranslationLayer


class ReviewCreateResponseReview(UniversalBaseModel):
    id: str
    game_id: typing_extensions.Annotated[str, FieldMetadata(alias="gameId"), pydantic.Field(alias="gameId")]
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    play_method: typing_extensions.Annotated[
        ReviewCreateResponseReviewPlayMethod, FieldMetadata(alias="playMethod"), pydantic.Field(alias="playMethod")
    ]
    translation_layer: typing_extensions.Annotated[
        typing.Optional[ReviewCreateResponseReviewTranslationLayer],
        FieldMetadata(alias="translationLayer"),
        pydantic.Field(alias="translationLayer"),
    ] = None
    performance: ReviewCreateResponseReviewPerformance
    fps: typing.Optional[float] = None
    graphics_settings: typing_extensions.Annotated[
        typing.Optional[ReviewCreateResponseReviewGraphicsSettings],
        FieldMetadata(alias="graphicsSettings"),
        pydantic.Field(alias="graphicsSettings"),
    ] = None
    resolution: typing.Optional[str] = None
    chipset: str
    chipset_variant: typing_extensions.Annotated[
        ReviewCreateResponseReviewChipsetVariant,
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
