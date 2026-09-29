

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mssql_rel_manual_native_query_config_insertion_order import MssqlRelManualNativeQueryConfigInsertionOrder


class MssqlRelManualNativeQueryConfig(UniversalBaseModel):
    column_mapping: typing.Dict[str, typing.Any]
    insertion_order: typing.Optional[MssqlRelManualNativeQueryConfigInsertionOrder] = None
    remote_native_query: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
