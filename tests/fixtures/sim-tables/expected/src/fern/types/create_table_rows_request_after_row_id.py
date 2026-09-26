

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_row_data import V2TableRowData


class CreateTableRowsRequestAfterRowId(UniversalBaseModel):
    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="Unique workspace identifier."),
    ]
    """
    Unique workspace identifier.
    """

    data: V2TableRowData = pydantic.Field()
    """
    Row cells keyed by column name.
    """

    after_row_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="afterRowId"),
        pydantic.Field(alias="afterRowId", description="Row after which to insert the new row."),
    ] = None
    """
    Row after which to insert the new row.
    """

    before_row_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="beforeRowId"),
        pydantic.Field(alias="beforeRowId", description="Row before which to insert the new row."),
    ] = None
    """
    Row before which to insert the new row.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
