

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId
from .snapshot import Snapshot


class ListSnapshotsResponse(UniversalBaseModel):
    """
    One page of snapshots, including expired snapshots that garbage collection hasn't deleted yet.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the snapshots belong to.
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    An opaque cursor for the next page.
    """

    snapshots: typing.List[Snapshot] = pydantic.Field()
    """
    The snapshot records, in ascending snapshot ID order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
