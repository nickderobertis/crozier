

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .cost import Cost
from .resource_description import ResourceDescription


class Armor(ApiReference, ResourceDescription):
    """
    `Armor`
    """

    armor_category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The category of armor this falls into.
    """

    armor_class: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Details on how to calculate armor class.
    """

    cost: typing.Optional[Cost] = None
    equipment_category: typing.Optional[ApiReference] = None
    stealth_disadvantage: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the armor gives disadvantage for Stealth.
    """

    str_minimum: typing.Optional[float] = pydantic.Field(default=None)
    """
    Minimum STR required to use this armor.
    """

    weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    How much the equipment weighs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
