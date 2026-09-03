

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetFapiStatusResponse(UniversalBaseModel):
    mode: typing.Optional[str] = None
    dpop_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="dpopEnabled"), pydantic.Field(alias="dpopEnabled")
    ] = None
    issuer: typing.Optional[str] = None
    fapi_modes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="fapiModes"), pydantic.Field(alias="fapiModes")
    ] = None
    dpop_nonce_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="dpopNonceRequired"), pydantic.Field(alias="dpopNonceRequired")
    ] = None
    dpop_nonce_duration: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="dpopNonceDuration"), pydantic.Field(alias="dpopNonceDuration")
    ] = None
    scope_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="scopeRequired"), pydantic.Field(alias="scopeRequired")
    ] = None
    refresh_token_kept: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="refreshTokenKept"), pydantic.Field(alias="refreshTokenKept")
    ] = None
    refresh_token_idempotent: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="refreshTokenIdempotent"),
        pydantic.Field(alias="refreshTokenIdempotent"),
    ] = None
    pkce_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="pkceRequired"), pydantic.Field(alias="pkceRequired")
    ] = None
    par_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="parRequired"), pydantic.Field(alias="parRequired")
    ] = None
    client_id_metadata_document_supported: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="clientIdMetadataDocumentSupported"),
        pydantic.Field(
            alias="clientIdMetadataDocumentSupported",
            description="Whether CIMD is enabled on the Authlete service (clientIdMetadataDocumentSupported)",
        ),
    ] = None
    """
    Whether CIMD is enabled on the Authlete service (clientIdMetadataDocumentSupported)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
