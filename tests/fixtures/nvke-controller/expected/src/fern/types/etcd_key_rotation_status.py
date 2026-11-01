

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .etcd_key_rotation_status_failure_reason import EtcdKeyRotationStatusFailureReason
from .etcd_key_rotation_status_phase import EtcdKeyRotationStatusPhase
from .etcd_key_rotation_status_state import EtcdKeyRotationStatusState


class EtcdKeyRotationStatus(UniversalBaseModel):
    """
    Durable status and retained ownership of an etcd data-encryption-key rotation.
    """

    workflow_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowID"),
        pydantic.Field(
            alias="workflowID",
            description="The Temporal workflow ID owning rotation and recovery. Never use as a metric label.",
        ),
    ]
    """
    The Temporal workflow ID owning rotation and recovery. Never use as a metric label.
    """

    state: EtcdKeyRotationStatusState = pydantic.Field()
    """
    Whether the owned rotation is running, succeeded, or failed.
    """

    phase: EtcdKeyRotationStatusPhase = pydantic.Field()
    """
    The last entered phase, which a failure retains. A `prepare` failure releases the mutation lock, so start a new rotation workflow after fixing it; a failure in a later phase keeps the lock for recovery of the owning workflow.
    """

    started_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="When rotation ownership was accepted by the controller."),
    ]
    """
    When rotation ownership was accepted by the controller.
    """

    last_progress_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastProgressAt"),
        pydantic.Field(
            alias="lastProgressAt",
            description="When a phase was entered or a terminal state was recorded. Polling does not advance it.",
        ),
    ]
    """
    When a phase was entered or a terminal state was recorded. Polling does not advance it.
    """

    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completedAt"),
        pydantic.Field(alias="completedAt", description="When the terminal success or failure was recorded."),
    ] = None
    """
    When the terminal success or failure was recorded.
    """

    failure_reason: typing_extensions.Annotated[
        typing.Optional[EtcdKeyRotationStatusFailureReason],
        FieldMetadata(alias="failureReason"),
        pydantic.Field(
            alias="failureReason",
            description="A bounded reason without keys, arbitrary error strings, or secret identifiers.",
        ),
    ] = None
    """
    A bounded reason without keys, arbitrary error strings, or secret identifiers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
