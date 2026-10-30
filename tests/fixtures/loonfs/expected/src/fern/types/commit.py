

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actor_id import ActorId
from .change_seq import ChangeSeq
from .commit_id import CommitId
from .filesystem_change import FilesystemChange
from .namespace_id import NamespaceId


class Commit(UniversalBaseModel):
    """
    One commit, including its identity and the events it applied.
    """

    commit_id: CommitId = pydantic.Field()
    """
    The commit's idempotency key.
    """

    committed_at_ms: int = pydantic.Field()
    """
    The time the commit was made, in Unix milliseconds. Commit order comes from `committed_seq`,
    not from this time.
    """

    committed_by: ActorId = pydantic.Field()
    """
    The actor responsible for the commit, as the application supplied it.
    """

    committed_seq: ChangeSeq = pydantic.Field()
    """
    The sequence at which the commit became visible.
    """

    events: typing.List[FilesystemChange] = pydantic.Field()
    """
    The semantic filesystem changes that the commit applied, in request order.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The caller's optional annotation for the commit.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
