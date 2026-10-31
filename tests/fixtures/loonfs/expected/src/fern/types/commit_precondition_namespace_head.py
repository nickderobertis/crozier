

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq


class CommitPreconditionNamespaceHead(UniversalBaseModel):
    """
    A requirement that the head sequence before the commit equals `expected_head_seq`.
    """

    expected_head_seq: ChangeSeq = pydantic.Field()
    """
    The head sequence that the caller observed when it read its inputs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
