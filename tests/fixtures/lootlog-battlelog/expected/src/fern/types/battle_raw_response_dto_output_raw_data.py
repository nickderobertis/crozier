

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_raw_response_dto_output_raw_data_events_item import BattleRawResponseDtoOutputRawDataEventsItem


class BattleRawResponseDtoOutputRawData(UniversalBaseModel):
    account_id: typing_extensions.Annotated[str, FieldMetadata(alias="accountId"), pydantic.Field(alias="accountId")]
    character_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="characterId"), pydantic.Field(alias="characterId")
    ]
    world: str
    events: typing.List[BattleRawResponseDtoOutputRawDataEventsItem]
    source_events: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="sourceEvents"),
        pydantic.Field(alias="sourceEvents"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
