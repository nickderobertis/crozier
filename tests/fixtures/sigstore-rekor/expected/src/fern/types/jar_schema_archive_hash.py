

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jar_schema_archive_hash_algorithm import JarSchemaArchiveHashAlgorithm


class JarSchemaArchiveHash(UniversalBaseModel):
    """
    Specifies the hash algorithm and value encompassing the entire signed archive
    """

    algorithm: JarSchemaArchiveHashAlgorithm = pydantic.Field()
    """
    The hashing function used to compute the hash value
    """

    value: str = pydantic.Field()
    """
    The hash value for the archive
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
