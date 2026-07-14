

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference


class OptionDamageDice(UniversalBaseModel):
    damage_dice: typing.Optional[str] = pydantic.Field(default=None)
    """
    Damage expressed in dice (e.g. "13d6").
    """

    damage_type: typing.Optional[ApiReference] = None
    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Information regarding the damage.
    """

    option_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option; determines other attributes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
