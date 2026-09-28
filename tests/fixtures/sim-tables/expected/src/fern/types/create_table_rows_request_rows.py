

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_row_data import V2TableRowData


class CreateTableRowsRequestRows(UniversalBaseModel):
    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="Unique workspace identifier."),
    ]
    """
    Unique workspace identifier.
    """

    rows: typing.List[V2TableRowData] = pydantic.Field()
    """
    Rows to insert, with cells keyed by column name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
