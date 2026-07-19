

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding_config import EmbeddingConfig


class SourceCreate(UniversalBaseModel):
    """
    Schema for creating a new Source.
    """

    name: str = pydantic.Field()
    """
    The name of the source.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the source.
    """

    instructions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Instructions for how to use the source.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Metadata associated with the source.
    """

    embedding: typing.Optional[str] = pydantic.Field(default=None)
    """
    The handle for the embedding config used by the source.
    """

    embedding_chunk_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The chunk size of the embedding.
    """

    embedding_config: typing.Optional[EmbeddingConfig] = pydantic.Field(default=None)
    """
    (Legacy) The embedding configuration used by the source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
