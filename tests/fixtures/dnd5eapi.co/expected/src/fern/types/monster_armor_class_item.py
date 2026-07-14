

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference


class MonsterArmorClassItem_Dex(UniversalBaseModel):
    """
    The armor class of a monster.
    """

    type: typing.Literal["dex"] = "dex"
    desc: typing.Optional[str] = None
    value: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MonsterArmorClassItem_Natural(UniversalBaseModel):
    """
    The armor class of a monster.
    """

    type: typing.Literal["natural"] = "natural"
    desc: typing.Optional[str] = None
    value: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MonsterArmorClassItem_Armor(UniversalBaseModel):
    """
    The armor class of a monster.
    """

    type: typing.Literal["armor"] = "armor"
    armor: typing.Optional[typing.List[ApiReference]] = None
    desc: typing.Optional[str] = None
    value: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MonsterArmorClassItem_Spell(UniversalBaseModel):
    """
    The armor class of a monster.
    """

    type: typing.Literal["spell"] = "spell"
    desc: typing.Optional[str] = None
    spell: typing.Optional[ApiReference] = None
    value: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MonsterArmorClassItem_Condition(UniversalBaseModel):
    """
    The armor class of a monster.
    """

    type: typing.Literal["condition"] = "condition"
    condition: typing.Optional[ApiReference] = None
    desc: typing.Optional[str] = None
    value: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MonsterArmorClassItem = typing_extensions.Annotated[
    typing.Union[
        MonsterArmorClassItem_Dex,
        MonsterArmorClassItem_Natural,
        MonsterArmorClassItem_Armor,
        MonsterArmorClassItem_Spell,
        MonsterArmorClassItem_Condition,
    ],
    pydantic.Field(discriminator="type"),
]
