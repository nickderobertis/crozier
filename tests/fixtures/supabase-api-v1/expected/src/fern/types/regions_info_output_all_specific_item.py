

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .regions_info_output_all_specific_item_code import RegionsInfoOutputAllSpecificItemCode
from .regions_info_output_all_specific_item_provider import RegionsInfoOutputAllSpecificItemProvider
from .regions_info_output_all_specific_item_status import RegionsInfoOutputAllSpecificItemStatus
from .regions_info_output_all_specific_item_type import RegionsInfoOutputAllSpecificItemType


class RegionsInfoOutputAllSpecificItem(UniversalBaseModel):
    name: str
    code: RegionsInfoOutputAllSpecificItemCode
    type: RegionsInfoOutputAllSpecificItemType
    provider: RegionsInfoOutputAllSpecificItemProvider
    status: typing.Optional[RegionsInfoOutputAllSpecificItemStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
