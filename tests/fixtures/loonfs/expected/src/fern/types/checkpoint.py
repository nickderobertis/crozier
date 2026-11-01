

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .checkpoint_owner import CheckpointOwner
from .manifest_no import ManifestNo
from .namespace_id import NamespaceId
from .pin_id import PinId


class Checkpoint(UniversalBaseModel):
    """
    One checkpoint, as its durable record stores it.
    """

    captured_seq: ChangeSeq = pydantic.Field()
    """
    The namespace sequence that the checkpoint captured.
    """

    checkpoint_id: PinId = pydantic.Field()
    """
    The checkpoint's durable ID. For a user pin, it's also the snapshot's `snapshot_id`.
    """

    created_at_ms: int = pydantic.Field()
    """
    The time the checkpoint record was created, in Unix milliseconds.
    """

    expires_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time the checkpoint expires, in Unix milliseconds. Garbage collection waits one more
    grace window before it deletes the record.
    """

    manifest_no: ManifestNo = pydantic.Field()
    """
    The manifest that the checkpoint pins.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the checkpoint belongs to.
    """

    owner: CheckpointOwner = pydantic.Field()
    """
    The checkpoint's owner. For a user pin, the owner includes the label.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
