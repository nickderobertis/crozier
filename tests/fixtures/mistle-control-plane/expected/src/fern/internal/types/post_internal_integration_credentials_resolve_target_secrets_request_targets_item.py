

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_integration_credentials_resolve_target_secrets_request_targets_item_encrypted_secrets import (
    PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItemEncryptedSecrets,
)


class PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem(UniversalBaseModel):
    target_key: typing_extensions.Annotated[str, FieldMetadata(alias="targetKey"), pydantic.Field(alias="targetKey")]
    encrypted_secrets: typing_extensions.Annotated[
        typing.Optional[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItemEncryptedSecrets],
        FieldMetadata(alias="encryptedSecrets"),
        pydantic.Field(alias="encryptedSecrets"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
