

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding_config import EmbeddingConfig
from .vector_db_provider import VectorDbProvider


class Source(UniversalBaseModel):
    """
    (Deprecated: Use Folder) Representation of a source, which is a collection of files and passages.
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

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Source
    """

    embedding_config: EmbeddingConfig = pydantic.Field()
    """
    The embedding configuration used by the source.
    """

    vector_db_provider: typing.Optional[VectorDbProvider] = pydantic.Field(default=None)
    """
    The vector database provider used for this source's passages
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this Tool.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this Tool.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the source was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the source was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
