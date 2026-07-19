

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tuf_schema_metadata import TufSchemaMetadata
from .tuf_schema_root import TufSchemaRoot


class TufSchema(UniversalBaseModel):
    """
    Schema for TUF metadata entries
    """

    spec_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    TUF specification version
    """

    metadata: TufSchemaMetadata = pydantic.Field()
    """
    TUF metadata
    """

    root: TufSchemaRoot = pydantic.Field()
    """
    root metadata containing about the public keys used to sign the manifest
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
