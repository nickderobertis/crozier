

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .monster_reactions_item_actions_item_type import MonsterReactionsItemActionsItemType


class MonsterReactionsItemActionsItem(UniversalBaseModel):
    action_name: typing.Optional[str] = None
    count: typing.Optional[float] = None
    type: typing.Optional[MonsterReactionsItemActionsItemType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
