

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_revision_no import AccessRevisionNo
from .attributes_revision_no import AttributesRevisionNo
from .binding_version import BindingVersion
from .change_seq import ChangeSeq
from .commit_id import CommitId
from .inode_id import InodeId
from .namespace_id import NamespaceId
from .revision_no import RevisionNo
from .writer_epoch import WriterEpoch
from .writer_id import WriterId


class ErrorDetails(UniversalBaseModel):
    """
    The machine-readable identifiers and state that explain an error response.

    Every field is optional.
    """

    active_acquired_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time the current writer acquired its epoch, in Unix milliseconds. It's present when the
    current manifest records a writer.
    """

    active_writer_epoch: typing.Optional[WriterEpoch] = pydantic.Field(default=None)
    """
    The namespace's current writer epoch.
    """

    active_writer_id: typing.Optional[WriterId] = pydantic.Field(default=None)
    """
    The writer of the current epoch. It's present when the current manifest records a writer.
    """

    actual_access_revision_no: typing.Optional[AccessRevisionNo] = pydantic.Field(default=None)
    """
    The access revision that is actually current for the inode.
    """

    actual_attributes_revision_no: typing.Optional[AttributesRevisionNo] = pydantic.Field(default=None)
    """
    The attribute revision that is actually current for the inode.
    """

    actual_binding_version: typing.Optional[BindingVersion] = pydantic.Field(default=None)
    """
    The current binding token.
    """

    actual_deletion_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The deletion sequence that is actually active for the inode.
    """

    actual_head_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The namespace's actual head sequence.
    """

    actual_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the path actually contained.
    """

    actual_revision_no: typing.Optional[RevisionNo] = pydantic.Field(default=None)
    """
    The revision that is actually current. It's absent when the inode has no current revision.
    """

    after_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The `after_seq` value from the change feed request.
    """

    commit_id: typing.Optional[CommitId] = pydantic.Field(default=None)
    """
    The idempotency key of the commit that the error is about.
    """

    committed_fingerprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fingerprint of the mutation that was committed under `commit_id`. This field is present
    exactly when `committed_seq` is present.
    """

    committed_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The sequence that `commit_id` was already committed at. The server includes it when a
    durable commit receipt records that commit.
    """

    expected_access_revision_no: typing.Optional[AccessRevisionNo] = pydantic.Field(default=None)
    """
    The access revision that the request expected to be current.
    """

    expected_attributes_revision_no: typing.Optional[AttributesRevisionNo] = pydantic.Field(default=None)
    """
    The attribute revision that the request expected to be current.
    """

    expected_binding_version: typing.Optional[BindingVersion] = pydantic.Field(default=None)
    """
    The opaque binding token that the request supplied.
    """

    expected_deletion_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The deletion sequence that the undelete expected to be active.
    """

    expected_head_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The head sequence that the request required.
    """

    expected_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the request expected the path to contain.
    """

    expected_revision_no: typing.Optional[RevisionNo] = pydantic.Field(default=None)
    """
    The revision that the request expected to be current.
    """

    fenced_writer_epoch: typing.Optional[WriterEpoch] = pydantic.Field(default=None)
    """
    The epoch of the failed writer session at the time another writer displaced it.
    """

    inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the failed precondition or operation targeted.
    """

    namespace_id: typing.Optional[NamespaceId] = pydantic.Field(default=None)
    """
    The deleted namespace that caused the operation to fail.
    """

    operation_index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the failed operation in the request.
    """

    precondition_index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The zero-based position of the failed request precondition.
    """

    retention_floor_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The namespace's retention floor. A change feed request can set `after_seq` to this sequence
    or any later one, and the feed returns the changes committed after it.
    """

    size_bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    For `range_not_satisfiable`, the size in bytes of the file that the range was requested
    from.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
