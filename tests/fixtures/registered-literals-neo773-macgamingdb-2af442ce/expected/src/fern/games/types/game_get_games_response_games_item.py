

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .game_get_games_response_games_item_performance_rating import GameGetGamesResponseGamesItemPerformanceRating


class GameGetGamesResponseGamesItem(UniversalBaseModel):
    id: str
    slug: typing.Optional[str] = None
    name: typing.Optional[str] = None
    header_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="headerImage"), pydantic.Field(alias="headerImage")
    ] = None
    release_year: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="releaseYear"), pydantic.Field(alias="releaseYear")
    ] = None
    performance_rating: typing_extensions.Annotated[
        GameGetGamesResponseGamesItemPerformanceRating,
        FieldMetadata(alias="performanceRating"),
        pydantic.Field(alias="performanceRating"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
