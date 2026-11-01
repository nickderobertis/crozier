

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId


class CheckpointOwnerFork(UniversalBaseModel):
    """
    A pin that keeps the source state that one fork attempt starts from.
    """

    target_namespace_id: NamespaceId = pydantic.Field()
    """
    The fork's target namespace. Garbage collection keeps this checkpoint while that
    namespace exists.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
