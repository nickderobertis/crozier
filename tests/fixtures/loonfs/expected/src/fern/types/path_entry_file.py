

import typing

import pydantic
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


class PathEntryFile(UniversalBaseModel):
    """
    A file, with a summary of its current revision.
    """

    attributes: typing.Optional[Attributes] = pydantic.Field(default=None)
    """
    The complete attribute map at `attributes_revision_no`. The map is empty before the first
    update.
    """

    attributes_revision_no: typing.Optional[AttributesRevisionNo] = pydantic.Field(default=None)
    """
    The attribute revision that these attributes come from.
    """

    attributes_updated_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time of the latest attribute update, in Unix milliseconds. It's absent before the first
    update.
    """

    attributes_updated_by: typing.Optional[ActorId] = pydantic.Field(default=None)
    """
    The actor responsible for the latest attribute update. It's absent before the first update.
    """

    binding_version: typing.Optional[BindingVersion] = pydantic.Field(default=None)
    """
    The opaque ID of the current binding of the entry's parent and name. It's absent for the
    namespace root.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The file's current content.
    """

    created_at_ms: int = pydantic.Field()
    """
    The time the inode was created, in Unix milliseconds.
    """

    created_by: ActorId = pydantic.Field()
    """
    The actor that created this inode, as the application supplied it.
    """

    display_name: typing.Optional[DisplayName] = pydantic.Field(default=None)
    """
    The stored display name of this path component. It's absent for the root, which has no name.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The namespace head sequence that this response was read at.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The entry's stable inode ID.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that was read.
    """

    parent_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The parent directory's inode. It's absent for the root.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path, built from the stored display names.
    """

    revision_committed_at_ms: int = pydantic.Field()
    """
    The time the current revision was committed, in Unix milliseconds.
    """

    revision_committed_by: ActorId = pydantic.Field()
    """
    The actor responsible for the current revision.
    """

    revision_no: RevisionNo = pydantic.Field()
    """
    The file's current revision number.
    """

    size_bytes: int = pydantic.Field()
    """
    The file's current size in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
