

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...core.serialization import FieldMetadata
from .update_table_view_request_config_sort_item import UpdateTableViewRequestConfigSortItem


class UpdateTableViewRequestConfig(UniversalBaseModel):
    """
    Complete replacement saved-view configuration.
    """

    column_widths: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, float]],
        FieldMetadata(alias="columnWidths"),
        pydantic.Field(
            alias="columnWidths", description="Column widths keyed by column name or stable column identifier."
        ),
    ] = None
    """
    Column widths keyed by column name or stable column identifier.
    """

    column_order: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="columnOrder"),
        pydantic.Field(alias="columnOrder", description="Columns in display order, by name or stable identifier."),
    ] = None
    """
    Columns in display order, by name or stable identifier.
    """

    pinned_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="pinnedColumns"),
        pydantic.Field(alias="pinnedColumns", description="Pinned columns, by name or stable identifier."),
    ] = None
    """
    Pinned columns, by name or stable identifier.
    """

    hidden_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="hiddenColumns"),
        pydantic.Field(alias="hiddenColumns", description="Hidden columns, by name or stable identifier."),
    ] = None
    """
    Hidden columns, by name or stable identifier.
    """

    filter: typing.Optional["TablePredicateInput"] = pydantic.Field(default=None)
    """
    Saved row predicate, or null when the view is unfiltered.
    """

    sort: typing.Optional[typing.List[UpdateTableViewRequestConfigSortItem]] = pydantic.Field(default=None)
    """
    Saved ordered sort specification, or null for default ordering.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from ...types.table_predicate_input import TablePredicateInput
from ...types.table_predicate_input_all import TablePredicateInputAll
from ...types.table_predicate_input_all_all_item import TablePredicateInputAllAllItem
from ...types.table_predicate_input_any import TablePredicateInputAny
from ...types.table_predicate_input_any_any_item import TablePredicateInputAnyAnyItem

update_forward_refs(
    UpdateTableViewRequestConfig,
    TablePredicateInput=TablePredicateInput,
    TablePredicateInputAll=TablePredicateInputAll,
    TablePredicateInputAllAllItem=TablePredicateInputAllAllItem,
    TablePredicateInputAny=TablePredicateInputAny,
    TablePredicateInputAnyAnyItem=TablePredicateInputAnyAnyItem,
)
