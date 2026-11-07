

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .game_get_by_id_response_stats_methods import GameGetByIdResponseStatsMethods
from .game_get_by_id_response_stats_translation_layers_value import GameGetByIdResponseStatsTranslationLayersValue


class GameGetByIdResponseStats(UniversalBaseModel):
    total_reviews: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalReviews"), pydantic.Field(alias="totalReviews")
    ]
    methods: GameGetByIdResponseStatsMethods
    average_performance: typing_extensions.Annotated[
        float, FieldMetadata(alias="averagePerformance"), pydantic.Field(alias="averagePerformance")
    ]
    translation_layers: typing_extensions.Annotated[
        typing.Dict[str, GameGetByIdResponseStatsTranslationLayersValue],
        FieldMetadata(alias="translationLayers"),
        pydantic.Field(alias="translationLayers"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
