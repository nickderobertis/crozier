

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chart_note_part_chart import ChartNotePartChart
from .entry_link import EntryLink
from .entry_table import EntryTable
from .inventory_container_table_note_part_mode import InventoryContainerTableNotePartMode
from .inventory_plate_table_note_part_mode import InventoryPlateTableNotePartMode
from .structured_table_column_info import StructuredTableColumnInfo


class EntryNotePart_AppCanvas(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["app_canvas"] = "app_canvas"
    app_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="appId"), pydantic.Field(alias="appId")
    ] = None
    canvas_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="canvasId"), pydantic.Field(alias="canvasId")
    ] = None
    feature_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="featureId"), pydantic.Field(alias="featureId")
    ] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_AssayRun(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["assay_run"] = "assay_run"
    assay_run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assayRunId"), pydantic.Field(alias="assayRunId")
    ] = None
    assay_run_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assayRunSchemaId"), pydantic.Field(alias="assayRunSchemaId")
    ] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_BoxCreationTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["box_creation_table"] = "box_creation_table"
    box_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="boxSchemaId"), pydantic.Field(alias="boxSchemaId")
    ] = None
    indentation: typing.Optional[int] = None
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_Code(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["code"] = "code"
    links: typing.Optional[typing.List[EntryLink]] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_ExternalFile(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["external_file"] = "external_file"
    external_file_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="externalFileId"), pydantic.Field(alias="externalFileId")
    ] = None
    links: typing.Optional[typing.List[EntryLink]] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_InventoryContainerTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["inventory_container_table"] = "inventory_container_table"
    destination_container_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationContainerSchemaId"),
        pydantic.Field(alias="destinationContainerSchemaId"),
    ] = None
    mode: typing.Optional[InventoryContainerTableNotePartMode] = None
    indentation: typing.Optional[int] = None
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_InventoryPlateTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["inventory_plate_table"] = "inventory_plate_table"
    destination_plate_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationPlateSchemaId"),
        pydantic.Field(alias="destinationPlateSchemaId"),
    ] = None
    destination_well_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationWellSchemaId"),
        pydantic.Field(alias="destinationWellSchemaId"),
    ] = None
    mode: typing.Optional[InventoryPlateTableNotePartMode] = None
    indentation: typing.Optional[int] = None
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_ListBullet(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["list_bullet"] = "list_bullet"
    links: typing.Optional[typing.List[EntryLink]] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_ListCheckbox(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["list_checkbox"] = "list_checkbox"
    checked: typing.Optional[bool] = None
    links: typing.Optional[typing.List[EntryLink]] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_ListNumber(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["list_number"] = "list_number"
    links: typing.Optional[typing.List[EntryLink]] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_LookupTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["lookup_table"] = "lookup_table"
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_MixturePrepTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["mixture_prep_table"] = "mixture_prep_table"
    mixture_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mixtureSchemaId"), pydantic.Field(alias="mixtureSchemaId")
    ] = None
    indentation: typing.Optional[int] = None
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_NoteLinkedChart(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["note_linked_chart"] = "note_linked_chart"
    chart: typing.Optional[ChartNotePartChart] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_PlateCreationTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["plate_creation_table"] = "plate_creation_table"
    plate_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="plateSchemaId"), pydantic.Field(alias="plateSchemaId")
    ] = None
    indentation: typing.Optional[int] = None
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_RegistrationTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["registration_table"] = "registration_table"
    entity_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="entitySchemaId"), pydantic.Field(alias="entitySchemaId")
    ] = None
    indentation: typing.Optional[int] = None
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_ResultsTable(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["results_table"] = "results_table"
    assay_result_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assayResultSchemaId"), pydantic.Field(alias="assayResultSchemaId")
    ] = None
    indentation: typing.Optional[int] = None
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_Table(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["table"] = "table"
    links: typing.Optional[typing.List[EntryLink]] = None
    table: typing.Optional[EntryTable] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_Text(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["text"] = "text"
    links: typing.Optional[typing.List[EntryLink]] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNotePart_TextBox(UniversalBaseModel):
    """
    Notes are the main building blocks of entries. Each note corresponds roughly to a paragraph.
    """

    type: typing.Literal["text_box"] = "text_box"
    links: typing.Optional[typing.List[EntryLink]] = None
    name: typing.Optional[str] = None
    text: typing.Optional[str] = None
    indentation: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


EntryNotePart = typing_extensions.Annotated[
    typing.Union[
        EntryNotePart_AppCanvas,
        EntryNotePart_AssayRun,
        EntryNotePart_BoxCreationTable,
        EntryNotePart_Code,
        EntryNotePart_ExternalFile,
        EntryNotePart_InventoryContainerTable,
        EntryNotePart_InventoryPlateTable,
        EntryNotePart_ListBullet,
        EntryNotePart_ListCheckbox,
        EntryNotePart_ListNumber,
        EntryNotePart_LookupTable,
        EntryNotePart_MixturePrepTable,
        EntryNotePart_NoteLinkedChart,
        EntryNotePart_PlateCreationTable,
        EntryNotePart_RegistrationTable,
        EntryNotePart_ResultsTable,
        EntryNotePart_Table,
        EntryNotePart_Text,
        EntryNotePart_TextBox,
    ],
    pydantic.Field(discriminator="type"),
]
