

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message import Message


class MessageSearchResult(UniversalBaseModel):
    """
    Result from a message search operation with scoring details.
    """

    embedded_text: str = pydantic.Field()
    """
    The embedded content (LLM-friendly)
    """

    message: Message = pydantic.Field()
    """
    The raw message object
    """

    fts_rank: typing.Optional[int] = pydantic.Field(default=None)
    """
    Full-text search rank position if FTS was used
    """

    vector_rank: typing.Optional[int] = pydantic.Field(default=None)
    """
    Vector search rank position if vector search was used
    """

    rrf_score: float = pydantic.Field()
    """
    Reciprocal Rank Fusion combined score
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
