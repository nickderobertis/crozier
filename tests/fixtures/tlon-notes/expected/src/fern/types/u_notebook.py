

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notebook import Notebook
from .u_folder import UFolder
from .u_member_joined_role import UMemberJoinedRole
from .u_nb_created_visibility import UNbCreatedVisibility
from .u_nb_visibility_changed_visibility import UNbVisibilityChangedVisibility
from .u_note import UNote


class UNotebook_NotebookCreated(UniversalBaseModel):
    type: typing.Literal["notebook-created"] = "notebook-created"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    notebook: Notebook
    visibility: UNbCreatedVisibility

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_NotebookUpdated(UniversalBaseModel):
    type: typing.Literal["notebook-updated"] = "notebook-updated"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    notebook: Notebook

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_NotebookDeleted(UniversalBaseModel):
    type: typing.Literal["notebook-deleted"] = "notebook-deleted"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_NotebookVisibilityChanged(UniversalBaseModel):
    type: typing.Literal["notebook-visibility-changed"] = "notebook-visibility-changed"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    visibility: UNbVisibilityChangedVisibility

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_MemberJoined(UniversalBaseModel):
    type: typing.Literal["member-joined"] = "member-joined"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    who: str
    role: UMemberJoinedRole

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_MemberLeft(UniversalBaseModel):
    type: typing.Literal["member-left"] = "member-left"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    who: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_InviteReceived(UniversalBaseModel):
    type: typing.Literal["invite-received"] = "invite-received"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_InviteRemoved(UniversalBaseModel):
    type: typing.Literal["invite-removed"] = "invite-removed"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_FolderUpdate(UniversalBaseModel):
    type: typing.Literal["folder-update"] = "folder-update"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    folder_update: typing_extensions.Annotated[
        UFolder, FieldMetadata(alias="folderUpdate"), pydantic.Field(alias="folderUpdate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNotebook_NoteUpdate(UniversalBaseModel):
    type: typing.Literal["note-update"] = "note-update"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    note_update: typing_extensions.Annotated[
        UNote, FieldMetadata(alias="noteUpdate"), pydantic.Field(alias="noteUpdate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UNotebook = typing_extensions.Annotated[
    typing.Union[
        UNotebook_NotebookCreated,
        UNotebook_NotebookUpdated,
        UNotebook_NotebookDeleted,
        UNotebook_NotebookVisibilityChanged,
        UNotebook_MemberJoined,
        UNotebook_MemberLeft,
        UNotebook_InviteReceived,
        UNotebook_InviteRemoved,
        UNotebook_FolderUpdate,
        UNotebook_NoteUpdate,
    ],
    pydantic.Field(discriminator="type"),
]
