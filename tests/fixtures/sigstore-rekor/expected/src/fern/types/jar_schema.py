

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jar_schema_archive import JarSchemaArchive
from .jar_schema_signature import JarSchemaSignature


class JarSchema(UniversalBaseModel):
    """
    Schema for JAR entries
    """

    signature: typing.Optional[JarSchemaSignature] = pydantic.Field(default=None)
    """
    Information about the included signature in the JAR file
    """

    archive: JarSchemaArchive = pydantic.Field()
    """
    Information about the archive associated with the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
