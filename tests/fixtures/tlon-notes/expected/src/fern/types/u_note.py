

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .note import Note
from .note_revision import NoteRevision


class UNote_NoteCreated(UniversalBaseModel):
    type: typing.Literal["note-created"] = "note-created"
    id: int
    note: Note

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNote_NoteUpdated(UniversalBaseModel):
    type: typing.Literal["note-updated"] = "note-updated"
    id: int
    note: Note

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNote_NoteDeleted(UniversalBaseModel):
    type: typing.Literal["note-deleted"] = "note-deleted"
    id: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNote_NotePublished(UniversalBaseModel):
    type: typing.Literal["note-published"] = "note-published"
    id: int
    html: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNote_NoteUnpublished(UniversalBaseModel):
    type: typing.Literal["note-unpublished"] = "note-unpublished"
    id: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UNote_NoteHistoryArchived(UniversalBaseModel):
    type: typing.Literal["note-history-archived"] = "note-history-archived"
    id: int
    revision: NoteRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UNote = typing_extensions.Annotated[
    typing.Union[
        UNote_NoteCreated,
        UNote_NoteUpdated,
        UNote_NoteDeleted,
        UNote_NotePublished,
        UNote_NoteUnpublished,
        UNote_NoteHistoryArchived,
    ],
    pydantic.Field(discriminator="type"),
]
