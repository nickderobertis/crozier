

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.v2table_row_data import V2TableRowData


class BulkUpdateTableRowsRequestUpdatesItem(UniversalBaseModel):
    row_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rowId"),
        pydantic.Field(alias="rowId", description="Identifier of the row this patch applies to."),
    ]
    """
    Identifier of the row this patch applies to.
    """

    data: V2TableRowData = pydantic.Field()
    """
    Cells to merge into this row, keyed by column name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
