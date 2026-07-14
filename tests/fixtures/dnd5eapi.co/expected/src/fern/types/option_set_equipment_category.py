

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference


class OptionSetEquipmentCategory(UniversalBaseModel):
    equipment_category: typing.Optional[ApiReference] = None
    option_set_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option set; determines other attributes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
