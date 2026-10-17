

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .regions_info_output_all_smart_group_item_code import RegionsInfoOutputAllSmartGroupItemCode
from .regions_info_output_all_smart_group_item_type import RegionsInfoOutputAllSmartGroupItemType


class RegionsInfoOutputAllSmartGroupItem(UniversalBaseModel):
    name: str
    code: RegionsInfoOutputAllSmartGroupItemCode
    type: RegionsInfoOutputAllSmartGroupItemType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
