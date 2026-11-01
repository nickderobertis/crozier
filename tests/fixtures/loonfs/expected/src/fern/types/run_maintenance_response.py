

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_revision_no import AccessRevisionNo
from .change_seq import ChangeSeq
from .commit_id import CommitId
from .deleted_checkpoints_by_owner import DeletedCheckpointsByOwner
from .deleted_object_counts import DeletedObjectCounts
from .extension_gc_reports import ExtensionGcReports
from .metadata_maintenance_outcome import MetadataMaintenanceOutcome
from .namespace_id import NamespaceId
from .retained_candidates import RetainedCandidates


class RunMaintenanceResponse_Gc(UniversalBaseModel):
    """
    The result of one maintenance job.

    The `kind` matches the request.
    """

    kind: typing.Literal["gc"] = "gc"
    deleted: DeletedObjectCounts
    deleted_checkpoints_by_owner: DeletedCheckpointsByOwner
    extensions: typing.Optional[ExtensionGcReports] = None
    listed_bytes: int
    namespace_id: NamespaceId
    next_reclamation_at_ms: typing.Optional[int] = None
    reclaimable_at_ms: typing.Optional[int] = None
    retained: RetainedCandidates

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceResponse_Metadata(UniversalBaseModel):
    """
    The result of one maintenance job.

    The `kind` matches the request.
    """

    kind: typing.Literal["metadata"] = "metadata"
    compaction_units: int
    namespace_id: NamespaceId
    outcome: MetadataMaintenanceOutcome

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceResponse_RecoverAdministrator(UniversalBaseModel):
    """
    The result of one maintenance job.

    The `kind` matches the request.
    """

    kind: typing.Literal["recover_administrator"] = "recover_administrator"
    access_revision_no: AccessRevisionNo
    commit_id: CommitId
    committed_seq: ChangeSeq
    namespace_id: NamespaceId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceResponse_Retention(UniversalBaseModel):
    """
    The result of one maintenance job.

    The `kind` matches the request.
    """

    kind: typing.Literal["retention"] = "retention"
    namespace_id: NamespaceId
    retention_floor_seq: ChangeSeq

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceResponse_RetentionWindow(UniversalBaseModel):
    """
    The result of one maintenance job.

    The `kind` matches the request.
    """

    kind: typing.Literal["retention_window"] = "retention_window"
    namespace_id: NamespaceId
    retention_window_ms: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunMaintenanceResponse = typing_extensions.Annotated[
    typing.Union[
        RunMaintenanceResponse_Gc,
        RunMaintenanceResponse_Metadata,
        RunMaintenanceResponse_RecoverAdministrator,
        RunMaintenanceResponse_Retention,
        RunMaintenanceResponse_RetentionWindow,
    ],
    pydantic.Field(discriminator="kind"),
]
