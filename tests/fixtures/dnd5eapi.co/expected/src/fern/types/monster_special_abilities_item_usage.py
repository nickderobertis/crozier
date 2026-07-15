

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .monster_special_abilities_item_usage_type import MonsterSpecialAbilitiesItemUsageType


class MonsterSpecialAbilitiesItemUsage(UniversalBaseModel):
    rest_types: typing.Optional[typing.List[str]] = None
    times: typing.Optional[float] = None
    type: typing.Optional[MonsterSpecialAbilitiesItemUsageType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
