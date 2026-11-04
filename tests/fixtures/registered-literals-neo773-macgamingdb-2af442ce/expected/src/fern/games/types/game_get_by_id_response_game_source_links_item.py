

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .game_get_by_id_response_game_source_links_item_source import GameGetByIdResponseGameSourceLinksItemSource


class GameGetByIdResponseGameSourceLinksItem(UniversalBaseModel):
    source: GameGetByIdResponseGameSourceLinksItemSource
    external_id: typing_extensions.Annotated[str, FieldMetadata(alias="externalId"), pydantic.Field(alias="externalId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
