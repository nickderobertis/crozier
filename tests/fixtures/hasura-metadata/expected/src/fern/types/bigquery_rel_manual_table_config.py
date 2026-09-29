

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .big_query_table_name import BigQueryTableName
from .bigquery_rel_manual_table_config_insertion_order import BigqueryRelManualTableConfigInsertionOrder


class BigqueryRelManualTableConfig(UniversalBaseModel):
    column_mapping: typing.Dict[str, typing.Any]
    insertion_order: typing.Optional[BigqueryRelManualTableConfigInsertionOrder] = None
    remote_table: BigQueryTableName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
