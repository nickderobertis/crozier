

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_in_progress_type import UpdateInProgressType


class UpdateInProgress(UniversalBaseModel):
    """
    The mutually exclusive cluster operation in progress. Absent when none.
    `etcd_key_rotation` is reported while an etcd data-encryption-key rotation
    holds the lock, and also after a rotation that failed after `prepare`,
    which keeps the lock until its owning workflow is recovered (see
    `conditions.etcdKeyRotation`). A `prepare` failure releases the lock.
    Exhaustive client switches over `type` must handle it.
    """

    type: UpdateInProgressType = pydantic.Field()
    """
    Operation in progress. `certificate_renewal` is reported while a
    scheduled or forced certificate-renewal cycle holds the lock, and
    also after a failed cycle whose lock is retained until an operator
    clears it. Clients that switch exhaustively over this value must
    handle it.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Detail.
    """

    started_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt", description="Start time.")
    ]
    """
    Start time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
