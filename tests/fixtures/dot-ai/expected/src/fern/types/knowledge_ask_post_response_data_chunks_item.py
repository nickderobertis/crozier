

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class KnowledgeAskPostResponseDataChunksItem(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    Chunk text content
    """

    uri: str = pydantic.Field()
    """
    Source document URI
    """

    score: float = pydantic.Field()
    """
    Relevance score from semantic search
    """

    chunk_index: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="chunkIndex"),
        pydantic.Field(alias="chunkIndex", description="Position of chunk within source document"),
    ]
    """
    Position of chunk within source document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
