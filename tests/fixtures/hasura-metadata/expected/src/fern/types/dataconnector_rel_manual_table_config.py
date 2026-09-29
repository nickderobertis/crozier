

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataconnector_rel_manual_table_config_insertion_order import DataconnectorRelManualTableConfigInsertionOrder


class DataconnectorRelManualTableConfig(UniversalBaseModel):
    column_mapping: typing.Dict[str, typing.Any]
    insertion_order: typing.Optional[DataconnectorRelManualTableConfigInsertionOrder] = None
    remote_table: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
