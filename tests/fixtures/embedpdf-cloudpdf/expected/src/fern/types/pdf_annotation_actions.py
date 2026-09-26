

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdf_action_tree import PdfActionTree


class PdfAnnotationActions(UniversalBaseModel):
    activate: typing.Optional[PdfActionTree] = None
    cursor_enter: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="cursorEnter"), pydantic.Field(alias="cursorEnter")
    ] = None
    cursor_exit: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="cursorExit"), pydantic.Field(alias="cursorExit")
    ] = None
    mouse_down: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="mouseDown"), pydantic.Field(alias="mouseDown")
    ] = None
    mouse_up: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="mouseUp"), pydantic.Field(alias="mouseUp")
    ] = None
    focus: typing.Optional[PdfActionTree] = None
    blur: typing.Optional[PdfActionTree] = None
    page_open: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="pageOpen"), pydantic.Field(alias="pageOpen")
    ] = None
    page_close: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="pageClose"), pydantic.Field(alias="pageClose")
    ] = None
    page_visible: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="pageVisible"), pydantic.Field(alias="pageVisible")
    ] = None
    page_invisible: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="pageInvisible"), pydantic.Field(alias="pageInvisible")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
