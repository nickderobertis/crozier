

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resolve_credentials_response_docker_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseDockerSource,
)
from .post_internal_sandbox_runtime_resolve_credentials_response_e2b_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseE2BSource,
)
from .post_internal_sandbox_runtime_resolve_credentials_response_modal_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseModalSource,
)
from .post_internal_sandbox_runtime_resolve_credentials_response_opencomputer_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseOpencomputerSource,
)
from .post_internal_sandbox_runtime_resolve_credentials_response_tensorlake_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseTensorlakeSource,
)


class PostInternalSandboxRuntimeResolveCredentialsResponse_Docker(UniversalBaseModel):
    provider: typing.Literal["docker"] = "docker"
    source: PostInternalSandboxRuntimeResolveCredentialsResponseDockerSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveCredentialsResponse_E2B(UniversalBaseModel):
    provider: typing.Literal["e2b"] = "e2b"
    source: PostInternalSandboxRuntimeResolveCredentialsResponseE2BSource
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")]
    domain: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveCredentialsResponse_Tensorlake(UniversalBaseModel):
    provider: typing.Literal["tensorlake"] = "tensorlake"
    source: PostInternalSandboxRuntimeResolveCredentialsResponseTensorlakeSource
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveCredentialsResponse_Opencomputer(UniversalBaseModel):
    provider: typing.Literal["opencomputer"] = "opencomputer"
    source: PostInternalSandboxRuntimeResolveCredentialsResponseOpencomputerSource
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")]
    api_base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiBaseUrl"), pydantic.Field(alias="apiBaseUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveCredentialsResponse_Modal(UniversalBaseModel):
    provider: typing.Literal["modal"] = "modal"
    source: PostInternalSandboxRuntimeResolveCredentialsResponseModalSource
    token_id: typing_extensions.Annotated[str, FieldMetadata(alias="tokenId"), pydantic.Field(alias="tokenId")]
    token_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="tokenSecret"), pydantic.Field(alias="tokenSecret")
    ]
    app_name: typing_extensions.Annotated[str, FieldMetadata(alias="appName"), pydantic.Field(alias="appName")]
    environment: typing.Optional[str] = None
    default_timeout_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="defaultTimeoutMs"), pydantic.Field(alias="defaultTimeoutMs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalSandboxRuntimeResolveCredentialsResponse = typing_extensions.Annotated[
    typing.Union[
        PostInternalSandboxRuntimeResolveCredentialsResponse_Docker,
        PostInternalSandboxRuntimeResolveCredentialsResponse_E2B,
        PostInternalSandboxRuntimeResolveCredentialsResponse_Tensorlake,
        PostInternalSandboxRuntimeResolveCredentialsResponse_Opencomputer,
        PostInternalSandboxRuntimeResolveCredentialsResponse_Modal,
    ],
    pydantic.Field(discriminator="provider"),
]
