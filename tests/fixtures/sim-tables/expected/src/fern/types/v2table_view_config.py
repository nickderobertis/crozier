

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_view_config_sort_item import V2TableViewConfigSortItem


class V2TableViewConfig(UniversalBaseModel):
    """
    Saved filter, sort, and column-layout settings for a table view.
    """

    column_widths: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, float]],
        FieldMetadata(alias="columnWidths"),
        pydantic.Field(alias="columnWidths", description="Column widths keyed by column name."),
    ] = None
    """
    Column widths keyed by column name.
    """

    column_order: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="columnOrder"),
        pydantic.Field(alias="columnOrder", description="Column names in display order."),
    ] = None
    """
    Column names in display order.
    """

    pinned_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="pinnedColumns"),
        pydantic.Field(alias="pinnedColumns", description="Names of pinned columns."),
    ] = None
    """
    Names of pinned columns.
    """

    hidden_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="hiddenColumns"),
        pydantic.Field(alias="hiddenColumns", description="Names of hidden columns."),
    ] = None
    """
    Names of hidden columns.
    """

    filter: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Saved row predicate, or null when the view is unfiltered.
    """

    sort: typing.Optional[typing.List[V2TableViewConfigSortItem]] = pydantic.Field(default=None)
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
