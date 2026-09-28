

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_row_data import V2TableRowData
from .v2table_row_run_state import V2TableRowRunState


class V2ApiTableRow(UniversalBaseModel):
    """
    A table row with user-defined cell values.
    """

    id: str = pydantic.Field()
    """
    Unique row identifier.
    """

    data: V2TableRowData = pydantic.Field()
    """
    Row cells keyed by column name.
    """

    run_state: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, V2TableRowRunState]],
        FieldMetadata(alias="runState"),
        pydantic.Field(
            alias="runState",
            description="Per-workflow-group run state keyed by group identifier. Present only when the read requested `includeRunState`.",
        ),
    ] = None
    """
    Per-workflow-group run state keyed by group identifier. Present only when the read requested `includeRunState`.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="ISO 8601 timestamp when the row was created."),
    ]
    """
    ISO 8601 timestamp when the row was created.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="ISO 8601 timestamp when the row was last modified."),
    ]
    """
    ISO 8601 timestamp when the row was last modified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
