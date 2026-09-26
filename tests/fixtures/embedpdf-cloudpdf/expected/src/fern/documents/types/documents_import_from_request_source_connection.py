

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class DocumentsImportFromRequestSourceConnection(UniversalBaseModel):
    """
    The operator pre-registered the authority: the request names a connection and a key inside it. Which provider backs the connection (S3, GCS, Azure Blob, filesystem, ...) is deployment configuration, never wire surface.
    """

    connection_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connectionId"),
        pydantic.Field(alias="connectionId", description="The operator-registered storage connection to read from."),
    ]
    """
    The operator-registered storage connection to read from.
    """

    key: str = pydantic.Field()
    """
    The object key to read, inside the connection's configured scope. At most 1024 UTF-8 bytes.
    """

    revision: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pins a specific version of the object. Provider-interpreted (S3 VersionId, GCS generation, Azure version id); providers without versioning reject it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
