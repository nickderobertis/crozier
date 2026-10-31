

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .absolute_path import AbsolutePath
from .access_grants import AccessGrants
from .access_revision_no import AccessRevisionNo
from .attribute_key import AttributeKey
from .attribute_value import AttributeValue
from .attributes_revision_no import AttributesRevisionNo
from .binding_version import BindingVersion
from .change_seq import ChangeSeq
from .content_ref import ContentRef
from .delete_directory_behavior import DeleteDirectoryBehavior
from .destination_behavior import DestinationBehavior
from .display_name import DisplayName
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperation_AppendFile(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["append_file"] = "append_file"
    expected_inode_id: typing.Optional[InodeId] = None
    expected_revision_no: typing.Optional[RevisionNo] = None
    inline_content: str
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_AppendFileByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["append_file_by_inode"] = "append_file_by_inode"
    expected_revision_no: typing.Optional[RevisionNo] = None
    inline_content: str
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_CopyByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["copy_by_inode"] = "copy_by_inode"
    behavior: typing.Optional[DestinationBehavior] = None
    destination_display_name: DisplayName
    destination_parent_inode_id: InodeId
    expected_destination_inode_id: typing.Optional[InodeId] = None
    expected_destination_revision_no: typing.Optional[RevisionNo] = None
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_CopyPath(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["copy_path"] = "copy_path"
    behavior: typing.Optional[DestinationBehavior] = None
    destination_path: AbsolutePath
    expected_destination_inode_id: typing.Optional[InodeId] = None
    expected_destination_revision_no: typing.Optional[RevisionNo] = None
    source_path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_CreateDirectory(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["create_directory"] = "create_directory"
    parents: typing.Optional[bool] = None
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_CreateDirectoryByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["create_directory_by_inode"] = "create_directory_by_inode"
    display_name: DisplayName
    parent_inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_CreateFileByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["create_file_by_inode"] = "create_file_by_inode"
    content_ref: typing.Optional[ContentRef] = None
    display_name: DisplayName
    inline_content: typing.Optional[str] = None
    parent_inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_DeleteByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["delete_by_inode"] = "delete_by_inode"
    behavior: typing.Optional[DeleteDirectoryBehavior] = None
    expected_binding_version: BindingVersion
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_DeletePath(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["delete_path"] = "delete_path"
    behavior: typing.Optional[DeleteDirectoryBehavior] = None
    expected_inode_id: typing.Optional[InodeId] = None
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_MoveByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["move_by_inode"] = "move_by_inode"
    behavior: typing.Optional[DestinationBehavior] = None
    destination_display_name: DisplayName
    destination_parent_inode_id: InodeId
    expected_binding_version: BindingVersion
    expected_destination_inode_id: typing.Optional[InodeId] = None
    expected_destination_revision_no: typing.Optional[RevisionNo] = None
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_MovePath(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["move_path"] = "move_path"
    behavior: typing.Optional[DestinationBehavior] = None
    destination_path: AbsolutePath
    expected_destination_inode_id: typing.Optional[InodeId] = None
    expected_destination_revision_no: typing.Optional[RevisionNo] = None
    source_path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_PutFile(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["put_file"] = "put_file"
    behavior: typing.Optional[DestinationBehavior] = None
    content_ref: typing.Optional[ContentRef] = None
    expected_inode_id: typing.Optional[InodeId] = None
    expected_revision_no: typing.Optional[RevisionNo] = None
    inline_content: typing.Optional[str] = None
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_PutFileRevisionByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["put_file_revision_by_inode"] = "put_file_revision_by_inode"
    content_ref: typing.Optional[ContentRef] = None
    expected_revision_no: RevisionNo
    inline_content: typing.Optional[str] = None
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_RestoreRevision(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["restore_revision"] = "restore_revision"
    path: AbsolutePath
    source_revision_no: RevisionNo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_RestoreRevisionByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["restore_revision_by_inode"] = "restore_revision_by_inode"
    inode_id: InodeId
    source_revision_no: RevisionNo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_Undelete(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["undelete"] = "undelete"
    deletion_seq: ChangeSeq
    destination_display_name: typing.Optional[DisplayName] = None
    destination_parent_inode_id: typing.Optional[InodeId] = None
    destination_path: typing.Optional[AbsolutePath] = None
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_UpdateAccess(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["update_access"] = "update_access"
    boundary: bool
    expected_access_revision_no: typing.Optional[AccessRevisionNo] = None
    expected_inode_id: typing.Optional[InodeId] = None
    grants: AccessGrants
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_UpdateAccessByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["update_access_by_inode"] = "update_access_by_inode"
    boundary: bool
    expected_access_revision_no: typing.Optional[AccessRevisionNo] = None
    grants: AccessGrants
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_UpdateAttributes(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["update_attributes"] = "update_attributes"
    expected_attributes_revision_no: typing.Optional[AttributesRevisionNo] = None
    expected_inode_id: typing.Optional[InodeId] = None
    path: AbsolutePath
    remove: typing.Optional[typing.List[AttributeKey]] = None
    set_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, AttributeValue]], FieldMetadata(alias="set"), pydantic.Field(alias="set")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilesystemOperation_UpdateAttributesByInode(UniversalBaseModel):
    """
    One filesystem operation.

    The server rejects unknown fields, and a variant without fields requires an empty object.
    """

    kind: typing.Literal["update_attributes_by_inode"] = "update_attributes_by_inode"
    expected_attributes_revision_no: typing.Optional[AttributesRevisionNo] = None
    inode_id: InodeId
    remove: typing.Optional[typing.List[AttributeKey]] = None
    set_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, AttributeValue]], FieldMetadata(alias="set"), pydantic.Field(alias="set")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FilesystemOperation = typing_extensions.Annotated[
    typing.Union[
        FilesystemOperation_AppendFile,
        FilesystemOperation_AppendFileByInode,
        FilesystemOperation_CopyByInode,
        FilesystemOperation_CopyPath,
        FilesystemOperation_CreateDirectory,
        FilesystemOperation_CreateDirectoryByInode,
        FilesystemOperation_CreateFileByInode,
        FilesystemOperation_DeleteByInode,
        FilesystemOperation_DeletePath,
        FilesystemOperation_MoveByInode,
        FilesystemOperation_MovePath,
        FilesystemOperation_PutFile,
        FilesystemOperation_PutFileRevisionByInode,
        FilesystemOperation_RestoreRevision,
        FilesystemOperation_RestoreRevisionByInode,
        FilesystemOperation_Undelete,
        FilesystemOperation_UpdateAccess,
        FilesystemOperation_UpdateAccessByInode,
        FilesystemOperation_UpdateAttributes,
        FilesystemOperation_UpdateAttributesByInode,
    ],
    pydantic.Field(discriminator="kind"),
]
