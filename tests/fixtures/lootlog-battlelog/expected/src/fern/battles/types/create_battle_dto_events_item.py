

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_battle_dto_events_item_f import CreateBattleDtoEventsItemF
from .create_battle_dto_events_item_match_summary import CreateBattleDtoEventsItemMatchSummary
from .create_battle_dto_events_item_party import CreateBattleDtoEventsItemParty


class CreateBattleDtoEventsItem(UniversalBaseModel):
    party: typing.Optional[CreateBattleDtoEventsItemParty] = None
    f: CreateBattleDtoEventsItemF
    ev: typing.Optional[float] = None
    match_summary: typing.Optional[CreateBattleDtoEventsItemMatchSummary] = None
    matchmaking_state: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
