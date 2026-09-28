

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_data_editor_data_column_sizing_mode import MarimoDataEditorDataColumnSizingMode
from .marimo_data_editor_data_data import MarimoDataEditorDataData
from .marimo_data_editor_data_editable_columns import MarimoDataEditorDataEditableColumns
from .marimo_data_editor_data_initial_value import MarimoDataEditorDataInitialValue


class MarimoDataEditorData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        MarimoDataEditorDataInitialValue, FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    label: typing.Optional[str] = None
    data: MarimoDataEditorDataData
    field_types: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[typing.Any]]],
        FieldMetadata(alias="fieldTypes"),
        pydantic.Field(alias="fieldTypes"),
    ] = None
    column_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="columnNames"), pydantic.Field(alias="columnNames")
    ] = None
    editable_columns: typing_extensions.Annotated[
        MarimoDataEditorDataEditableColumns,
        FieldMetadata(alias="editableColumns"),
        pydantic.Field(alias="editableColumns"),
    ]
    column_sizing_mode: typing_extensions.Annotated[
        typing.Optional[MarimoDataEditorDataColumnSizingMode],
        FieldMetadata(alias="columnSizingMode"),
        pydantic.Field(alias="columnSizingMode"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
