

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .a_folder import AFolder
from .a_note import ANote
from .nb_batch_import_notes_item import NbBatchImportNotesItem
from .nb_visibility_visibility import NbVisibilityVisibility


class ANotebook_Rename(UniversalBaseModel):
    type: typing.Literal["rename"] = "rename"
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_Delete(UniversalBaseModel):
    type: typing.Literal["delete"] = "delete"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_Visibility(UniversalBaseModel):
    type: typing.Literal["visibility"] = "visibility"
    visibility: NbVisibilityVisibility

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_Invite(UniversalBaseModel):
    type: typing.Literal["invite"] = "invite"
    who: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_CreateFolder(UniversalBaseModel):
    type: typing.Literal["create-folder"] = "create-folder"
    parent: typing.Optional[int] = None
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_Folder(UniversalBaseModel):
    type: typing.Literal["folder"] = "folder"
    id: int
    action: AFolder

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_CreateNote(UniversalBaseModel):
    type: typing.Literal["create-note"] = "create-note"
    folder: int
    title: str
    body: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_Note(UniversalBaseModel):
    type: typing.Literal["note"] = "note"
    id: int
    action: ANote

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_BatchImport(UniversalBaseModel):
    type: typing.Literal["batch-import"] = "batch-import"
    folder: int
    notes: typing.List[NbBatchImportNotesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANotebook_BatchImportTree(UniversalBaseModel):
    type: typing.Literal["batch-import-tree"] = "batch-import-tree"
    parent: int
    tree: typing.List["ImportNode"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ANotebook = typing_extensions.Annotated[
    typing.Union[
        ANotebook_Rename,
        ANotebook_Delete,
        ANotebook_Visibility,
        ANotebook_Invite,
        ANotebook_CreateFolder,
        ANotebook_Folder,
        ANotebook_CreateNote,
        ANotebook_Note,
        ANotebook_BatchImport,
        ANotebook_BatchImportTree,
    ],
    pydantic.Field(discriminator="type"),
]
from .import_node import ImportNode
from .import_node_children import ImportNodeChildren

update_forward_refs(ANotebook_BatchImportTree, ImportNode=ImportNode, ImportNodeChildren=ImportNodeChildren)
