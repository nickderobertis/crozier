

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeletedObjectCounts(UniversalBaseModel):
    """
    The number of objects that one garbage collection pass deleted, grouped by object family.
    """

    content_objects: int = pydantic.Field()
    """
    The content objects the pass deleted because no retained view referenced them and they were
    older than the grace window.
    """

    manifests: int = pydantic.Field()
    """
    The unreferenced manifests that the pass deleted.
    """

    metadata_segments: int = pydantic.Field()
    """
    The unreferenced metadata segments that the pass deleted.
    """

    retired_content_objects: int = pydantic.Field()
    """
    The content objects that the pass listed under a retired namespace and deleted.
    """

    temporary_objects: int = pydantic.Field()
    """
    The store's temporary objects that the pass deleted because they were older than the grace
    window.
    """

    upload_sessions: int = pydantic.Field()
    """
    The upload session records that the pass deleted after their grace windows passed.
    """

    wal_objects: int = pydantic.Field()
    """
    The unreferenced WAL objects that the pass deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
