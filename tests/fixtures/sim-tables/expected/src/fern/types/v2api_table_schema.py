

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2api_table_schema_columns_item import V2ApiTableSchemaColumnsItem


class V2ApiTableSchema(UniversalBaseModel):
    """
    Typed table schema.
    """

    columns: typing.List[V2ApiTableSchemaColumnsItem] = pydantic.Field()
    """
    Table column definitions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
