

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MonsterSpecialAbilitiesItemSpellcastingSpellsItem(UniversalBaseModel):
    level: typing.Optional[float] = None
    name: typing.Optional[str] = None
    url: typing.Optional[str] = None
    usage: typing.Optional[typing.Optional[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
