

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2api_table_row import V2ApiTableRow
from .v2upsert_row_data_operation import V2UpsertRowDataOperation


class V2UpsertRowData(UniversalBaseModel):
    """
    Row returned by an upsert and the operation performed.
    """

    row: V2ApiTableRow = pydantic.Field()
    """
    The inserted or updated table row.
    """

    operation: V2UpsertRowDataOperation = pydantic.Field()
    """
    Whether the row was inserted or updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
