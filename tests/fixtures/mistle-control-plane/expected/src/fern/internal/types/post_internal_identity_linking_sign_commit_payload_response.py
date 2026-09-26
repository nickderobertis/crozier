

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_identity_linking_sign_commit_payload_response_format import (
    PostInternalIdentityLinkingSignCommitPayloadResponseFormat,
)
from .post_internal_identity_linking_sign_commit_payload_response_signature_encoding import (
    PostInternalIdentityLinkingSignCommitPayloadResponseSignatureEncoding,
)


class PostInternalIdentityLinkingSignCommitPayloadResponse(UniversalBaseModel):
    format: PostInternalIdentityLinkingSignCommitPayloadResponseFormat
    signature: str
    signature_encoding: typing_extensions.Annotated[
        PostInternalIdentityLinkingSignCommitPayloadResponseSignatureEncoding,
        FieldMetadata(alias="signatureEncoding"),
        pydantic.Field(alias="signatureEncoding"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
