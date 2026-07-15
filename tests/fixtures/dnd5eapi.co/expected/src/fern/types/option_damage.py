

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .damage import Damage
from .dc import Dc


class OptionDamage(UniversalBaseModel):
    damage: typing.Optional[typing.List[Damage]] = pydantic.Field(default=None)
    """
    Damage dealt by the breath attack, if any.
    """

    dc: typing.Optional[Dc] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the breath
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
