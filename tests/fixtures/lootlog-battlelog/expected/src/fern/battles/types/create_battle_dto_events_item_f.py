

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_battle_dto_events_item_fw_value import CreateBattleDtoEventsItemFwValue


class CreateBattleDtoEventsItemF(UniversalBaseModel):
    m: typing.Optional[typing.List[str]] = None
    end_battle: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="endBattle"), pydantic.Field(alias="endBattle")
    ] = None
    init: typing.Optional[str] = None
    auto: typing.Optional[str] = None
    w: typing.Optional[typing.Dict[str, CreateBattleDtoEventsItemFwValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
