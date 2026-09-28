

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_code_editor_data_debounce import MarimoCodeEditorDataDebounce
from .marimo_code_editor_data_theme import MarimoCodeEditorDataTheme


class MarimoCodeEditorData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    language: typing.Optional[str] = None
    placeholder: str
    theme: typing.Optional[MarimoCodeEditorDataTheme] = None
    label: typing.Optional[str] = None
    disabled: typing.Optional[bool] = None
    min_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minHeight"), pydantic.Field(alias="minHeight")
    ] = None
    max_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxHeight"), pydantic.Field(alias="maxHeight")
    ] = None
    show_copy_button: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showCopyButton"), pydantic.Field(alias="showCopyButton")
    ] = None
    debounce: typing.Optional[MarimoCodeEditorDataDebounce] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
