

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .cost import Cost
from .resource_description import ResourceDescription


class Gear(ApiReference, ResourceDescription):
    """
    `Gear`
    """

    cost: typing.Optional[Cost] = None
    equipment_category: typing.Optional[ApiReference] = None
    gear_category: typing.Optional[ApiReference] = None
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
