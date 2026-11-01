

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .namespace_id import NamespaceId


class NamespaceForkBasis(UniversalBaseModel):
    """
    The source namespace and sequence that a forked namespace started from.
    """

    source_head_seq: ChangeSeq = pydantic.Field()
    """
    The source namespace's sequence that the fork captured.
    """

    source_namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the fork was taken from.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
