

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_extraction_query_attribute_groups_item_filter_item_codes_item import (
    DataExtractionQueryAttributeGroupsItemFilterItemCodesItem,
)


class DataExtractionQueryAttributeGroupsItemFilterItem(UniversalBaseModel):
    type: str
    name: str
    codes: typing.Optional[typing.List[DataExtractionQueryAttributeGroupsItemFilterItemCodesItem]] = None
    start: typing.Optional[dt.date] = None
    end: typing.Optional[dt.date] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
