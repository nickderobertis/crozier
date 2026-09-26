

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_table_data_data import MarimoTableDataData
from .marimo_table_data_initial_value import MarimoTableDataInitialValue
from .marimo_table_data_max_columns import MarimoTableDataMaxColumns
from .marimo_table_data_raw_data import MarimoTableDataRawData
from .marimo_table_data_selection import MarimoTableDataSelection
from .marimo_table_data_show_column_summaries import MarimoTableDataShowColumnSummaries
from .marimo_table_data_text_justify_columns_value import MarimoTableDataTextJustifyColumnsValue
from .marimo_table_data_total_rows import MarimoTableDataTotalRows


class MarimoTableData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        MarimoTableDataInitialValue, FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    label: typing.Optional[str] = None
    data: MarimoTableDataData
    raw_data: typing_extensions.Annotated[
        typing.Optional[MarimoTableDataRawData], FieldMetadata(alias="rawData"), pydantic.Field(alias="rawData")
    ] = None
    total_rows: typing_extensions.Annotated[
        MarimoTableDataTotalRows, FieldMetadata(alias="totalRows"), pydantic.Field(alias="totalRows")
    ]
    pagination: typing.Optional[bool] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    selection: typing.Optional[MarimoTableDataSelection] = None
    show_download: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showDownload"), pydantic.Field(alias="showDownload")
    ] = None
    show_filters: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showFilters"), pydantic.Field(alias="showFilters")
    ] = None
    show_column_summaries: typing_extensions.Annotated[
        typing.Optional[MarimoTableDataShowColumnSummaries],
        FieldMetadata(alias="showColumnSummaries"),
        pydantic.Field(alias="showColumnSummaries"),
    ] = None
    show_data_types: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showDataTypes"), pydantic.Field(alias="showDataTypes")
    ] = None
    show_page_size_selector: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showPageSizeSelector"), pydantic.Field(alias="showPageSizeSelector")
    ] = None
    show_column_explorer: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showColumnExplorer"), pydantic.Field(alias="showColumnExplorer")
    ] = None
    show_row_explorer: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showRowExplorer"), pydantic.Field(alias="showRowExplorer")
    ] = None
    show_chart_builder: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showChartBuilder"), pydantic.Field(alias="showChartBuilder")
    ] = None
    show_search: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showSearch"), pydantic.Field(alias="showSearch")
    ] = None
    row_headers: typing_extensions.Annotated[
        typing.List[typing.List[typing.Any]], FieldMetadata(alias="rowHeaders"), pydantic.Field(alias="rowHeaders")
    ]
    freeze_columns_left: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="freezeColumnsLeft"),
        pydantic.Field(alias="freezeColumnsLeft"),
    ] = None
    freeze_columns_right: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="freezeColumnsRight"),
        pydantic.Field(alias="freezeColumnsRight"),
    ] = None
    hidden_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="hiddenColumns"), pydantic.Field(alias="hiddenColumns")
    ] = None
    text_justify_columns: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, MarimoTableDataTextJustifyColumnsValue]],
        FieldMetadata(alias="textJustifyColumns"),
        pydantic.Field(alias="textJustifyColumns"),
    ] = None
    wrapped_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="wrappedColumns"), pydantic.Field(alias="wrappedColumns")
    ] = None
    column_widths: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="columnWidths"),
        pydantic.Field(alias="columnWidths"),
    ] = None
    header_tooltip: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="headerTooltip"),
        pydantic.Field(alias="headerTooltip"),
    ] = None
    field_types: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[typing.Any]]],
        FieldMetadata(alias="fieldTypes"),
        pydantic.Field(alias="fieldTypes"),
    ] = None
    total_columns: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalColumns"), pydantic.Field(alias="totalColumns")
    ]
    max_columns: typing_extensions.Annotated[
        typing.Optional[MarimoTableDataMaxColumns],
        FieldMetadata(alias="maxColumns"),
        pydantic.Field(alias="maxColumns"),
    ] = None
    has_stable_row_id: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasStableRowId"), pydantic.Field(alias="hasStableRowId")
    ] = None
    max_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxHeight"), pydantic.Field(alias="maxHeight")
    ] = None
    cell_styles: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, typing.Any]]]],
        FieldMetadata(alias="cellStyles"),
        pydantic.Field(alias="cellStyles"),
    ] = None
    hover_template: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hoverTemplate"), pydantic.Field(alias="hoverTemplate")
    ] = None
    cell_hover_texts: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, typing.Optional[str]]]],
        FieldMetadata(alias="cellHoverTexts"),
        pydantic.Field(alias="cellHoverTexts"),
    ] = None
    lazy: typing.Optional[bool] = None
    preload: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
