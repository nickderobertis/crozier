

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column_config import ColumnConfig
from .export_response_tables_item_configuration import ExportResponseTablesItemConfiguration


class ExportResponseTablesItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    configuration: typing.Optional[ExportResponseTablesItemConfiguration] = None
    columns: typing.Optional[typing.List[ColumnConfig]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
