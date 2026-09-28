

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_button_data_kind import MarimoButtonDataKind


class MarimoButtonData(UniversalBaseModel):
    label: str
    kind: typing.Optional[MarimoButtonDataKind] = None
    disabled: typing.Optional[bool] = None
    full_width: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fullWidth"), pydantic.Field(alias="fullWidth")
    ] = None
    tooltip: typing.Optional[str] = None
    keyboard_shortcut: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="keyboardShortcut"), pydantic.Field(alias="keyboardShortcut")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
