

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actor_id import ActorId
from .change_seq import ChangeSeq
from .manifest_no import ManifestNo
from .namespace_fork_basis import NamespaceForkBasis
from .namespace_id import NamespaceId


class NamespaceDiagnostics(UniversalBaseModel):
    """
    A namespace's state and the storage details that maintenance uses.
    """

    acknowledged_floor_seq: ChangeSeq = pydantic.Field()
    """
    The highest retention floor that a WAL object folded into the current manifest was
    validated against. It's at most `retention_floor_seq`, and it stays below a new floor until
    a WAL object validated against that floor is folded.
    """

    created_at_ms: int = pydantic.Field()
    """
    The time the namespace was created, in Unix milliseconds.
    """

    created_by: ActorId = pydantic.Field()
    """
    The actor that created the namespace, as the application supplied it.
    """

    current_manifest_no: typing.Optional[ManifestNo] = pydantic.Field(default=None)
    """
    The number of the namespace's current manifest.
    """

    fork_basis: typing.Optional[NamespaceForkBasis] = pydantic.Field(default=None)
    """
    The namespace and sequence this namespace was forked from. Only a forked namespace has this
    field.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The sequence of the namespace's newest visible commit.
    """

    live_snapshots: int = pydantic.Field()
    """
    The number of snapshots that hadn't expired when the diagnostics read began.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace ID.
    """

    retention_floor_seq: ChangeSeq = pydantic.Field()
    """
    The namespace's retention floor. A change feed request can set `after_seq` to this sequence
    or any later one, and the feed returns the changes committed after it.
    """

    wal_tail_objects: int = pydantic.Field()
    """
    The number of visible WAL objects after the current manifest.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
