

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .column_description import ColumnDescription
from .error_info import ErrorInfo
from .query_status import QueryStatus
from .secondary_id_id import SecondaryIdId


class FullExecutionStatus(QueryStatus):
    progress: typing.Optional[float] = pydantic.Field(default=None)
    """
    Progress of the query.
    """

    column_descriptions: typing_extensions.Annotated[
        typing.Optional[typing.List[ColumnDescription]],
        FieldMetadata(alias="columnDescriptions"),
        pydantic.Field(alias="columnDescriptions", description="Metadata of the queries result by column."),
    ] = None
    """
    Metadata of the queries result by column.
    """

    can_expand: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="canExpand"),
        pydantic.Field(
            alias="canExpand",
            description="Flag for the frontend, if the query can be rendered by it and therefore should allow expansion.",
        ),
    ] = None
    """
    Flag for the frontend, if the query can be rendered by it and therefore should allow expansion.
    """

    query: typing.Optional["Query"] = None
    error: typing.Optional[ErrorInfo] = None
    available_secondary_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[SecondaryIdId]],
        FieldMetadata(alias="availableSecondaryIds"),
        pydantic.Field(
            alias="availableSecondaryIds",
            description="List of all secondaryIds available inside this query, this is used by the frontend to display them to users when reusing queries.",
        ),
    ] = None
    """
    List of all secondaryIds available inside this query, this is used by the frontend to display them to users when reusing queries.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .absolute_form_query import AbsoluteFormQuery
from .entity_date_query import EntityDateQuery
from .query import Query
from .relative_form_query import RelativeFormQuery
from .table_export_query import TableExportQuery

update_forward_refs(
    FullExecutionStatus,
    AbsoluteFormQuery=AbsoluteFormQuery,
    EntityDateQuery=EntityDateQuery,
    Query=Query,
    RelativeFormQuery=RelativeFormQuery,
    TableExportQuery=TableExportQuery,
)
