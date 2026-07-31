

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .folder import Folder


class UFolder_FolderCreated(UniversalBaseModel):
    type: typing.Literal["folder-created"] = "folder-created"
    id: int
    folder: Folder

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UFolder_FolderUpdated(UniversalBaseModel):
    type: typing.Literal["folder-updated"] = "folder-updated"
    id: int
    folder: Folder

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UFolder_FolderDeleted(UniversalBaseModel):
    type: typing.Literal["folder-deleted"] = "folder-deleted"
    id: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UFolder = typing_extensions.Annotated[
    typing.Union[UFolder_FolderCreated, UFolder_FolderUpdated, UFolder_FolderDeleted],
    pydantic.Field(discriminator="type"),
]
