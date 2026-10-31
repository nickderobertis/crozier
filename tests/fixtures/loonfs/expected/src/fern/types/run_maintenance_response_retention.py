

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .namespace_id import NamespaceId


class RunMaintenanceResponseRetention(UniversalBaseModel):
    """
    The result of advancing the retention floor.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace whose retention floor was advanced.
    """

    retention_floor_seq: ChangeSeq = pydantic.Field()
    """
    The retention floor that the advance reached, which is the minimum sequence for incremental
    replay. It's below the target when LoonFS reads a commit that's less than one hour old
    before it reaches the target.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
