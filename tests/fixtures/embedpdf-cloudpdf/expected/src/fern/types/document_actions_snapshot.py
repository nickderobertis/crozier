

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .document_actions_snapshot_name_tree_scripts_item import DocumentActionsSnapshotNameTreeScriptsItem
from .pdf_action_tree import PdfActionTree
from .pdf_destination import PdfDestination


class DocumentActionsSnapshot(UniversalBaseModel):
    name_tree_scripts: typing_extensions.Annotated[
        typing.List[DocumentActionsSnapshotNameTreeScriptsItem],
        FieldMetadata(alias="nameTreeScripts"),
        pydantic.Field(alias="nameTreeScripts"),
    ]
    open_action: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="openAction"), pydantic.Field(alias="openAction")
    ] = None
    open_destination: typing_extensions.Annotated[
        typing.Optional[PdfDestination], FieldMetadata(alias="openDestination"), pydantic.Field(alias="openDestination")
    ] = None
    will_close: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="willClose"), pydantic.Field(alias="willClose")
    ] = None
    will_save: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="willSave"), pydantic.Field(alias="willSave")
    ] = None
    did_save: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="didSave"), pydantic.Field(alias="didSave")
    ] = None
    will_print: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="willPrint"), pydantic.Field(alias="willPrint")
    ] = None
    did_print: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="didPrint"), pydantic.Field(alias="didPrint")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
