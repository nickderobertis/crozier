

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding_config import EmbeddingConfig


class Folder(UniversalBaseModel):
    """
    Representation of a folder, which is a collection of files and passages.
    """

    name: str = pydantic.Field()
    """
    The name of the folder.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the folder.
    """

    instructions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Instructions for how to use the folder.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Metadata associated with the folder.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Source
    """

    embedding_config: EmbeddingConfig = pydantic.Field()
    """
    The embedding configuration used by the folder.
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
    The timestamp when the folder was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the folder was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
