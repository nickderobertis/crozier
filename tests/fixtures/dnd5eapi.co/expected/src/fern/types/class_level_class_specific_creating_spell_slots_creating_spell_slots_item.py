

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClassLevelClassSpecificCreatingSpellSlotsCreatingSpellSlotsItem(UniversalBaseModel):
    sorcery_point_cost: typing.Optional[float] = None
    spell_slot_level: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
