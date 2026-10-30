

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_grants import AccessGrants
from .access_revision_no import AccessRevisionNo
from .attributes import Attributes
from .attributes_revision_no import AttributesRevisionNo
from .binding_version import BindingVersion
from .content_ref import ContentRef
from .directory_binding import DirectoryBinding
from .display_name import DisplayName
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemChange_AccessChanged(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["access_changed"] = "access_changed"
    access_revision_no: AccessRevisionNo
    boundary: bool
    grants: AccessGrants
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemChange_AttributesChanged(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["attributes_changed"] = "attributes_changed"
    attributes: Attributes
    attributes_revision_no: AttributesRevisionNo
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemChange_ContentChanged(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["content_changed"] = "content_changed"
    append_offset: typing.Optional[int] = None
    content_ref: ContentRef
    inode_id: InodeId
    revision_no: RevisionNo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemChange_Deleted(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["deleted"] = "deleted"
    deleted_binding: DirectoryBinding
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemChange_DirectoryCreated(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["directory_created"] = "directory_created"
    binding_version: BindingVersion
    display_name: DisplayName
    inode_id: InodeId
    parent_inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemChange_FileCreated(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["file_created"] = "file_created"
    binding_version: BindingVersion
    content_ref: ContentRef
    display_name: DisplayName
    inode_id: InodeId
    parent_inode_id: InodeId
    revision_no: RevisionNo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemChange_Moved(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["moved"] = "moved"
    binding_version: BindingVersion
    destination_display_name: DisplayName
    destination_parent_inode_id: InodeId
    inode_id: InodeId
    source_display_name: DisplayName
    source_parent_inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemChange_Undeleted(UniversalBaseModel):
    """
    One filesystem change within a commit.

    One request operation can produce several changes.

    A newer server can return a change kind that isn't listed here. Clients should skip a change
    whose kind they don't recognize.
    """

    kind: typing.Literal["undeleted"] = "undeleted"
    binding_version: BindingVersion
    display_name: DisplayName
    inode_id: InodeId
    parent_inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FilesystemChange = typing_extensions.Annotated[
    typing.Union[
        FilesystemChange_AccessChanged,
        FilesystemChange_AttributesChanged,
        FilesystemChange_ContentChanged,
        FilesystemChange_Deleted,
        FilesystemChange_DirectoryCreated,
        FilesystemChange_FileCreated,
        FilesystemChange_Moved,
        FilesystemChange_Undeleted,
    ],
    pydantic.Field(discriminator="kind"),
]
