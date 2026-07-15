

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference
from .spell_prerequisite import SpellPrerequisite


class SubclassSpellsItem(UniversalBaseModel):
    prerequisites: typing.Optional[typing.List[SpellPrerequisite]] = None
    spell: typing.Optional[ApiReference] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
