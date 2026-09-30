

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column_config import ColumnConfig
from .graph_ql_name import GraphQlName
from .table_custom_root_fields import TableCustomRootFields


class CitusTableConfig(UniversalBaseModel):
    column_config: typing.Optional[typing.Dict[str, ColumnConfig]] = None
    comment: typing.Optional[str] = None
    custom_column_names: typing.Optional[typing.Dict[str, GraphQlName]] = None
    custom_name: typing.Optional[GraphQlName] = None
    custom_root_fields: typing.Optional[TableCustomRootFields] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
