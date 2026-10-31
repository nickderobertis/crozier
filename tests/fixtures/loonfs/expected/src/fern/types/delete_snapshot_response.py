

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId
from .pin_id import PinId


class DeleteSnapshotResponse(UniversalBaseModel):
    """
    The snapshot record that was deleted.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the snapshot belonged to.
    """

    snapshot_id: PinId = pydantic.Field()
    """
    The ID of the deleted snapshot record.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
