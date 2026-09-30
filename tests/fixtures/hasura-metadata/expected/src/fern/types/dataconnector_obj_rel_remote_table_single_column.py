

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataconnector_obj_rel_remote_table_single_column_column import DataconnectorObjRelRemoteTableSingleColumnColumn


class DataconnectorObjRelRemoteTableSingleColumn(UniversalBaseModel):
    column: DataconnectorObjRelRemoteTableSingleColumnColumn
    table: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
