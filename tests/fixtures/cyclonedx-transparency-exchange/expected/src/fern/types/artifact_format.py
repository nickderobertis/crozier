

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .checksum import Checksum


class ArtifactFormat(UniversalBaseModel):
    """
    A security-related document in a specific format
    """

    media_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mediaType"),
        pydantic.Field(alias="mediaType", description="The Media Type of the document"),
    ] = None
    """
    The Media Type of the document
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A free text describing the TEA Artifact
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Direct download URL for the TEA Artifact
    """

    signature_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signatureUrl"),
        pydantic.Field(
            alias="signatureUrl", description="Direct download URL for an external signature of the TEA Artifact"
        ),
    ] = None
    """
    Direct download URL for an external signature of the TEA Artifact
    """

    checksums: typing.Optional[typing.List[Checksum]] = pydantic.Field(default=None)
    """
    List of checksums for the TEA Artifact
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
