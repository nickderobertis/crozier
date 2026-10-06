

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_battle_dto_events_item_party_members_value import CreateBattleDtoEventsItemPartyMembersValue


class CreateBattleDtoEventsItemParty(UniversalBaseModel):
    members: typing.Dict[str, CreateBattleDtoEventsItemPartyMembersValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
