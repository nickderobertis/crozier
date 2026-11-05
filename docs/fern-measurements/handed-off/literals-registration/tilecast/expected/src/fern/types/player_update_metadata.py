

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .player_family import PlayerFamily
from .player_update_metadata_architecture import PlayerUpdateMetadataArchitecture
from .player_update_metadata_platform import PlayerUpdateMetadataPlatform


class PlayerUpdateMetadata(UniversalBaseModel):
    release_id: typing_extensions.Annotated[str, FieldMetadata(alias="releaseId"), pydantic.Field(alias="releaseId")]
    artifact_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="artifactId"),
        pydantic.Field(alias="artifactId", description="The artifact's asset name."),
    ] = None
    """
    The artifact's asset name.
    """

    platform: PlayerUpdateMetadataPlatform
    version_code: typing_extensions.Annotated[
        int, FieldMetadata(alias="versionCode"), pydantic.Field(alias="versionCode")
    ]
    version_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="versionName"), pydantic.Field(alias="versionName")
    ]
    player_family: typing_extensions.Annotated[
        typing.Optional[PlayerFamily], FieldMetadata(alias="playerFamily"), pydantic.Field(alias="playerFamily")
    ] = None
    architecture: typing.Optional[PlayerUpdateMetadataArchitecture] = pydantic.Field(default=None)
    """
    Tilecast Edge only.
    """

    artifact_size_bytes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="artifactSizeBytes"),
        pydantic.Field(alias="artifactSizeBytes", description="Linux families."),
    ] = None
    """
    Linux families.
    """

    artifact_sha256: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="artifactSha256"),
        pydantic.Field(alias="artifactSha256", description="Linux families."),
    ] = None
    """
    Linux families.
    """

    artifact_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="artifactPath"),
        pydantic.Field(
            alias="artifactPath", description="`/api/v1/player/updates/{releaseId}/artifact` for the Linux families."
        ),
    ] = None
    """
    `/api/v1/player/updates/{releaseId}/artifact` for the Linux families.
    """

    signed_manifest: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signedManifest"),
        pydantic.Field(
            alias="signedManifest",
            description="Tilecast Edge only: the exact bytes of the signed update envelope, base64. The screen verifies the signature and every field against this answer and its `install_player_update` command before it downloads.",
        ),
    ] = None
    """
    Tilecast Edge only: the exact bytes of the signed update envelope, base64. The screen verifies the signature and every field against this answer and its `install_player_update` command before it downloads.
    """

    manifest_signature: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="manifestSignature"),
        pydantic.Field(
            alias="manifestSignature", description="Tilecast Edge only. The envelope's base64 Ed25519 signature text."
        ),
    ] = None
    """
    Tilecast Edge only. The envelope's base64 Ed25519 signature text.
    """

    state_schema_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="stateSchemaVersion"),
        pydantic.Field(
            alias="stateSchemaVersion",
            description="Tilecast Edge only. The state database schema the release migrates to.",
        ),
    ] = None
    """
    Tilecast Edge only. The state database schema the release migrates to.
    """

    application_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="applicationId"),
        pydantic.Field(alias="applicationId", description="Android only."),
    ] = None
    """
    Android only.
    """

    minimum_sdk: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minimumSdk"),
        pydantic.Field(alias="minimumSdk", description="Android only."),
    ] = None
    """
    Android only.
    """

    apk_size_bytes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="apkSizeBytes"),
        pydantic.Field(alias="apkSizeBytes", description="Android only."),
    ] = None
    """
    Android only.
    """

    apk_sha256: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apkSha256"),
        pydantic.Field(alias="apkSha256", description="Android only."),
    ] = None
    """
    Android only.
    """

    signing_certificate_sha256: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signingCertificateSha256"),
        pydantic.Field(alias="signingCertificateSha256", description="Android only."),
    ] = None
    """
    Android only.
    """

    apk_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apkPath"),
        pydantic.Field(alias="apkPath", description="Android only."),
    ] = None
    """
    Android only.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
