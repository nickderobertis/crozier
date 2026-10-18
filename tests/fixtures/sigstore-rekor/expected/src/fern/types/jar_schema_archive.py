

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jar_schema_archive_hash import JarSchemaArchiveHash


class JarSchemaArchive(UniversalBaseModel):
    """
    Information about the archive associated with the entry
    """

    hash: typing.Optional[JarSchemaArchiveHash] = pydantic.Field(default=None)
    """
    Specifies the hash algorithm and value encompassing the entire signed archive
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the archive inline within the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
