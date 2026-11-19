

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reconcile_state import ReconcileState


class ReconcileStatus(UniversalBaseModel):
    """
    Whether a dataset's lineage-graph version matches its actual on-disk Lance version (#23).

    ``dangling_blob_columns`` (§9 P1 lifecycle, 2026-07-12) is the POINTER-health axis the version
    comparison can't see: a blob-v2 column whose payloads no longer dereference (external object
    deleted, bucket wiped) leaves the version untouched — a dataset can be ``in_sync`` and still
    unreadable. Non-empty = those columns failed a real 1-byte probe read.
    """

    dangling_blob_columns: typing.Optional[typing.List[str]] = None
    dataset: str
    graph_version: typing.Optional[int] = None
    in_sync: bool
    missing_declared_columns: typing.Optional[typing.List[str]] = None
    stale: typing.Optional[bool] = None
    status: ReconcileState
    storage_version: typing.Optional[int] = None
    unreadable_reason: typing.Optional[str] = None
    unrecorded_bases: typing.Optional[typing.List[str]] = None
    versions_without_lineage: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
