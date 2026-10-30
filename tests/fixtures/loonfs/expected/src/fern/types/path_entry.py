

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .actor_id import ActorId
from .attributes import Attributes
from .attributes_revision_no import AttributesRevisionNo
from .binding_version import BindingVersion
from .change_seq import ChangeSeq
from .content_ref import ContentRef
from .display_name import DisplayName
from .inode_id import InodeId
from .namespace_id import NamespaceId
from .revision_no import RevisionNo


class PathEntry_Dir(UniversalBaseModel):
    """
    The metadata for one path, as stat and directory listings return it.

    The response includes attribute fields only when the request asks for them.

    A newer server can return an inode kind that isn't listed here. Clients should read only the
    fields that every entry includes.
    """

    inode_kind: typing.Literal["dir"] = "dir"
    attributes: typing.Optional[Attributes] = None
    attributes_revision_no: typing.Optional[AttributesRevisionNo] = None
    attributes_updated_at_ms: typing.Optional[int] = None
    attributes_updated_by: typing.Optional[ActorId] = None
    binding_version: typing.Optional[BindingVersion] = None
    created_at_ms: int
    created_by: ActorId
    display_name: typing.Optional[DisplayName] = None
    head_seq: ChangeSeq
    inode_id: InodeId
    namespace_id: NamespaceId
    parent_inode_id: typing.Optional[InodeId] = None
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PathEntry_File(UniversalBaseModel):
    """
    The metadata for one path, as stat and directory listings return it.

    The response includes attribute fields only when the request asks for them.

    A newer server can return an inode kind that isn't listed here. Clients should read only the
    fields that every entry includes.
    """

    inode_kind: typing.Literal["file"] = "file"
    attributes: typing.Optional[Attributes] = None
    attributes_revision_no: typing.Optional[AttributesRevisionNo] = None
    attributes_updated_at_ms: typing.Optional[int] = None
    attributes_updated_by: typing.Optional[ActorId] = None
    binding_version: typing.Optional[BindingVersion] = None
    content_ref: ContentRef
    created_at_ms: int
    created_by: ActorId
    display_name: typing.Optional[DisplayName] = None
    head_seq: ChangeSeq
    inode_id: InodeId
    namespace_id: NamespaceId
    parent_inode_id: typing.Optional[InodeId] = None
    path: AbsolutePath
    revision_committed_at_ms: int
    revision_committed_by: ActorId
    revision_no: RevisionNo
    size_bytes: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PathEntry = typing_extensions.Annotated[
    typing.Union[PathEntry_Dir, PathEntry_File], pydantic.Field(discriminator="inode_kind")
]
