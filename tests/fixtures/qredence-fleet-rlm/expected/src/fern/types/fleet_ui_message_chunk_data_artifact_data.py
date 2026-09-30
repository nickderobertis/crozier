

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FleetUiMessageChunkDataArtifactData(UniversalBaseModel):
    artifact_id: str
    artifact_kind: typing.Optional[str] = None
    kind: typing.Optional[str] = None
    title: typing.Optional[str] = None
    name: typing.Optional[str] = None
    media_type: typing.Optional[str] = None
    media_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")
    ] = None
    byte_size: typing.Optional[int] = None
    byte_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="byteSize"), pydantic.Field(alias="byteSize")
    ] = None
    checksum_sha256: typing.Optional[str] = None
    checksum_sha256: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="checksumSha256"), pydantic.Field(alias="checksumSha256")
    ] = None
    artifact_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="artifactId"), pydantic.Field(alias="artifactId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
