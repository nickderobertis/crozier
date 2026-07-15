

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference
from .spellcasting_info_item import SpellcastingInfoItem


class Spellcasting(UniversalBaseModel):
    """
    `Spellcasting`
    """

    info: typing.Optional[typing.List[SpellcastingInfoItem]] = pydantic.Field(default=None)
    """
    Descriptions of the class' ability to cast spells.
    """

    level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Level at which the class can start using its spellcasting abilities.
    """

    spellcasting_ability: typing.Optional[ApiReference] = pydantic.Field(default=None)
    """
    Reference to the `AbilityScore` used for spellcasting by the class.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
