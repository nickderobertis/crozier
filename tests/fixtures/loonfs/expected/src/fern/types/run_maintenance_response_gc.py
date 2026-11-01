

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deleted_checkpoints_by_owner import DeletedCheckpointsByOwner
from .deleted_object_counts import DeletedObjectCounts
from .extension_gc_reports import ExtensionGcReports
from .namespace_id import NamespaceId
from .retained_candidates import RetainedCandidates


class RunMaintenanceResponseGc(UniversalBaseModel):
    """
    The counts and deadlines from one garbage collection call.
    """

    deleted: DeletedObjectCounts = pydantic.Field()
    """
    The objects that the pass deleted, counted by object family.
    """

    deleted_checkpoints_by_owner: DeletedCheckpointsByOwner = pydantic.Field()
    """
    The checkpoint records that the pass deleted, counted by owner.
    """

    extensions: typing.Optional[ExtensionGcReports] = pydantic.Field(default=None)
    """
    The reports from the extension collectors, each under its extension's name, left out when
    no extension collector ran.
    
    After the core collector, a `gc` run runs the collector of each extension whose state the
    deployment maintains. For example, a deployment that advertises `maintenance.grep.index`
    reports the counts of the grep index's collector in `extensions.grep`.
    """

    listed_bytes: int = pydantic.Field()
    """
    The bytes of every object that the pass listed under the namespace, each object once, before
    the pass's deletes.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the pass ran against.
    """

    next_reclamation_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The earliest future retirement deadline, pin deletion time, or upload cleanup time.
    """

    reclaimable_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The deletion time of the current tombstone plus the configured retirement grace.
    """

    retained: RetainedCandidates = pydantic.Field()
    """
    The candidates that the pass kept at deletion time, counted by reason.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
