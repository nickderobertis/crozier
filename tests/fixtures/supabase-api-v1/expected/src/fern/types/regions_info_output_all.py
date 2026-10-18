

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .regions_info_output_all_smart_group_item import RegionsInfoOutputAllSmartGroupItem
from .regions_info_output_all_specific_item import RegionsInfoOutputAllSpecificItem


class RegionsInfoOutputAll(UniversalBaseModel):
    smart_group: typing_extensions.Annotated[
        typing.List[RegionsInfoOutputAllSmartGroupItem],
        FieldMetadata(alias="smartGroup"),
        pydantic.Field(alias="smartGroup"),
    ]
    specific: typing.List[RegionsInfoOutputAllSpecificItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
