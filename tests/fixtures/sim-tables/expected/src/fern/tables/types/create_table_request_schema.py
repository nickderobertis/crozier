

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_table_request_schema_columns_item import CreateTableRequestSchemaColumnsItem


class CreateTableRequestSchema(UniversalBaseModel):
    """
    Initial table column definitions.
    """

    columns: typing.List[CreateTableRequestSchemaColumnsItem] = pydantic.Field()
    """
    Initial table columns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
