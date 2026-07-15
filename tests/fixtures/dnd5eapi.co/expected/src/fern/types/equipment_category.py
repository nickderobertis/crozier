

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference


class EquipmentCategory(ApiReference):
    """
    `EquipmentCategory`
    """

    equipment: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    A list of the equipment that falls into this category.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
