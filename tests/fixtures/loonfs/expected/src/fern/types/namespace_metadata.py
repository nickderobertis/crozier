

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actor_id import ActorId
from .change_seq import ChangeSeq
from .namespace_access_mode import NamespaceAccessMode
from .namespace_fork_basis import NamespaceForkBasis
from .namespace_id import NamespaceId


class NamespaceMetadata(UniversalBaseModel):
    """
    The current state of one namespace.
    """

    access: NamespaceAccessMode = pydantic.Field()
    """
    The namespace's access mode.
    """

    created_at_ms: int = pydantic.Field()
    """
    The time the namespace was created, in Unix milliseconds.
    """

    created_by: ActorId = pydantic.Field()
    """
    The actor that created the namespace, as the application supplied it.
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

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace ID.
    """

    retention_floor_seq: ChangeSeq = pydantic.Field()
    """
    The namespace's retention floor. A change feed request can set `after_seq` to this sequence
    or any later one, and the feed returns the changes committed after it.
    """

    retention_window_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The namespace's retention window, in milliseconds. Only a namespace with its own window has
    this field. The reference server's maintenance sweep uses the server's `retention_window_ms`
    setting for a namespace that has no window of its own.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
