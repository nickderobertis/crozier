

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataconnector_obj_rel_remote_table_multiple_columns_columns_item import (
    DataconnectorObjRelRemoteTableMultipleColumnsColumnsItem,
)


class DataconnectorObjRelRemoteTableMultipleColumns(UniversalBaseModel):
    columns: typing.List[DataconnectorObjRelRemoteTableMultipleColumnsColumnsItem]
    table: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
