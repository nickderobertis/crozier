

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_integration_credentials_resolve_target_secrets_response_targets_item import (
    PostInternalIntegrationCredentialsResolveTargetSecretsResponseTargetsItem,
)


class PostInternalIntegrationCredentialsResolveTargetSecretsResponse(UniversalBaseModel):
    targets: typing.List[PostInternalIntegrationCredentialsResolveTargetSecretsResponseTargetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
