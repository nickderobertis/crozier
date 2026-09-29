

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataconnector_arr_rel_using_f_key_on_multiple_columns_columns_item import (
    DataconnectorArrRelUsingFKeyOnMultipleColumnsColumnsItem,
)


class DataconnectorArrRelUsingFKeyOnMultipleColumns(UniversalBaseModel):
    columns: typing.List[DataconnectorArrRelUsingFKeyOnMultipleColumnsColumnsItem]
    table: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
