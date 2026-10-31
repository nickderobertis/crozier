

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeletedCheckpointsByOwner(UniversalBaseModel):
    """
    The number of checkpoint records that one garbage collection pass deleted, grouped by owner.
    """

    fork: int = pydantic.Field()
    """
    The fork pins that the pass deleted because their target namespaces no longer exist.
    """

    user: int = pydantic.Field()
    """
    The user pins that the pass deleted after they expired or their namespace was deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
