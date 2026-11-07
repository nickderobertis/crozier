

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .game_search_response_item_source import GameSearchResponseItemSource


class GameSearchResponseItem(UniversalBaseModel):
    ref: str
    source: GameSearchResponseItemSource
    name: str
    slug: typing.Optional[str] = None
    cover_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="coverImage"), pydantic.Field(alias="coverImage")
    ] = None
    release_year: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="releaseYear"), pydantic.Field(alias="releaseYear")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
