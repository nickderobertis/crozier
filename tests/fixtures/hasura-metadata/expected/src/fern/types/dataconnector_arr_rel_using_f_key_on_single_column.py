

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataconnector_arr_rel_using_f_key_on_single_column_column import DataconnectorArrRelUsingFKeyOnSingleColumnColumn


class DataconnectorArrRelUsingFKeyOnSingleColumn(UniversalBaseModel):
    column: DataconnectorArrRelUsingFKeyOnSingleColumnColumn
    table: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
