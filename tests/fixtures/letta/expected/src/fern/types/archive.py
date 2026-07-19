

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding_config import EmbeddingConfig
from .vector_db_provider import VectorDbProvider


class Archive(UniversalBaseModel):
    """
    Representation of an archive - a collection of archival passages that can be shared between agents.
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The creation date of the archive
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was last updated.
    """

    name: str = pydantic.Field()
    """
    The name of the archive
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the archive
    """

    vector_db_provider: typing.Optional[VectorDbProvider] = pydantic.Field(default=None)
    """
    The vector database provider used for this archive's passages
    """

    embedding_config: typing.Optional[EmbeddingConfig] = pydantic.Field(default=None)
    """
    Embedding configuration for passages in this archive
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional metadata
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Archive
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
