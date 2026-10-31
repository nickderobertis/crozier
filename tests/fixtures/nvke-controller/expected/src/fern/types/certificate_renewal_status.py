

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .certificate_renewal_status_outcome import CertificateRenewalStatusOutcome
from .certificate_renewal_status_state import CertificateRenewalStatusState


class CertificateRenewalStatus(UniversalBaseModel):
    """
    The recorded lifecycle state and outcome of a certificate-renewal cycle.
    """

    cycle_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="cycleID"),
        pydantic.Field(
            alias="cycleID", description="The Temporal workflow ID that owns this certificate-renewal cycle."
        ),
    ]
    """
    The Temporal workflow ID that owns this certificate-renewal cycle.
    """

    state: CertificateRenewalStatusState = pydantic.Field()
    """
    The lifecycle state of the most recent certificate-renewal cycle.
    """

    outcome: typing.Optional[CertificateRenewalStatusOutcome] = pydantic.Field(default=None)
    """
    Whether a successful cycle renewed certificates or found no certificates due.
    """

    forced: bool = pydantic.Field()
    """
    Whether the workflow was explicitly forced by an operator.
    """

    scheduled_for: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="scheduledFor"),
        pydantic.Field(
            alias="scheduledFor", description="The scheduled due time associated with this cycle, when applicable."
        ),
    ] = None
    """
    The scheduled due time associated with this cycle, when applicable.
    """

    started_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startedAt"),
        pydantic.Field(
            alias="startedAt",
            description="When the workflow accepted the cycle and acquired the cluster mutation lock. Refused cycles record startedAt without holding the lock.",
        ),
    ]
    """
    When the workflow accepted the cycle and acquired the cluster mutation lock. Refused cycles record startedAt without holding the lock.
    """

    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completedAt"),
        pydantic.Field(alias="completedAt", description="When the cycle succeeded or failed."),
    ] = None
    """
    When the cycle succeeded or failed.
    """

    failed_node_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="failedNodeID"),
        pydantic.Field(
            alias="failedNodeID",
            description="The control-plane node being processed when the cycle failed, when applicable.",
        ),
    ] = None
    """
    The control-plane node being processed when the cycle failed, when applicable.
    """

    phase: typing.Optional[str] = pydantic.Field(default=None)
    """
    The workflow phase that failed, when applicable.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A bounded operator-facing failure summary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
