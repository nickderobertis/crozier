

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .game_get_by_id_response_game_aggregated_performance import GameGetByIdResponseGameAggregatedPerformance
from .game_get_by_id_response_game_source_links_item import GameGetByIdResponseGameSourceLinksItem


class GameGetByIdResponseGame(UniversalBaseModel):
    id: str
    slug: typing.Optional[str] = None
    name: str
    header_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="headerImage"), pydantic.Field(alias="headerImage")
    ] = None
    description_html: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="descriptionHtml"), pydantic.Field(alias="descriptionHtml")
    ] = None
    website: typing.Optional[str] = None
    release_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="releaseDate"), pydantic.Field(alias="releaseDate")
    ] = None
    release_year: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="releaseYear"), pydantic.Field(alias="releaseYear")
    ] = None
    developers: typing.Optional[typing.List[str]] = None
    publishers: typing.Optional[typing.List[str]] = None
    genres: typing.Optional[typing.List[str]] = None
    screenshots: typing.Optional[typing.List[str]] = None
    source_links: typing_extensions.Annotated[
        typing.List[GameGetByIdResponseGameSourceLinksItem],
        FieldMetadata(alias="sourceLinks"),
        pydantic.Field(alias="sourceLinks"),
    ]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    aggregated_performance: typing_extensions.Annotated[
        typing.Optional[GameGetByIdResponseGameAggregatedPerformance],
        FieldMetadata(alias="aggregatedPerformance"),
        pydantic.Field(alias="aggregatedPerformance"),
    ] = None
    review_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="reviewCount"), pydantic.Field(alias="reviewCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
