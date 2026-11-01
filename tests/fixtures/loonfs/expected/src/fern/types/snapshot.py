

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .namespace_id import NamespaceId
from .pin_id import PinId


class Snapshot(UniversalBaseModel):
    """
    A snapshot, which keeps one version of a namespace readable until it's deleted or expires.
    """

    captured_seq: ChangeSeq = pydantic.Field()
    """
    The namespace sequence that the snapshot captured.
    """

    created_at_ms: int = pydantic.Field()
    """
    The time the snapshot record was created, in Unix milliseconds.
    """

    expires_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time the snapshot expires, in Unix milliseconds. A snapshot without it doesn't expire.
    An expired snapshot can't be read, and it's listed until garbage collection deletes it.
    """

    name: str = pydantic.Field()
    """
    The snapshot's label.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace whose state the snapshot captured.
    """

    snapshot_id: PinId = pydantic.Field()
    """
    The snapshot ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
