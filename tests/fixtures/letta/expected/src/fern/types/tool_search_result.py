

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool import Tool


class ToolSearchResult(UniversalBaseModel):
    """
    Result from a tool search operation.
    """

    tool: Tool = pydantic.Field()
    """
    The matched tool.
    """

    embedded_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The embedded text content used for matching.
    """

    fts_rank: typing.Optional[int] = pydantic.Field(default=None)
    """
    Full-text search rank position.
    """

    vector_rank: typing.Optional[int] = pydantic.Field(default=None)
    """
    Vector search rank position.
    """

    combined_score: float = pydantic.Field()
    """
    Combined relevance score (RRF for hybrid mode).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
