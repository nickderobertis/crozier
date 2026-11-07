

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .library_list_response_item_aggregated_performance import LibraryListResponseItemAggregatedPerformance


class LibraryListResponseItem(UniversalBaseModel):
    external_game_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="externalGameId"), pydantic.Field(alias="externalGameId")
    ]
    name: typing.Optional[str] = None
    icon_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="iconHash"), pydantic.Field(alias="iconHash")
    ] = None
    playtime_minutes: typing_extensions.Annotated[
        float, FieldMetadata(alias="playtimeMinutes"), pydantic.Field(alias="playtimeMinutes")
    ]
    aggregated_performance: typing_extensions.Annotated[
        typing.Optional[LibraryListResponseItemAggregatedPerformance],
        FieldMetadata(alias="aggregatedPerformance"),
        pydantic.Field(alias="aggregatedPerformance"),
    ] = None
    review_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="reviewCount"), pydantic.Field(alias="reviewCount")
    ]
    has_data: typing_extensions.Annotated[bool, FieldMetadata(alias="hasData"), pydantic.Field(alias="hasData")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
