

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .requests_filter_type import RequestsFilterType
from .scoped_uuid import ScopedUuid
from .unscoped_uuid import UnscopedUuid


class AllFilterItems_AiPlugin(UniversalBaseModel):
    field: typing.Literal["ai_plugin"] = "ai_plugin"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_AiProvider(UniversalBaseModel):
    field: typing.Literal["ai_provider"] = "ai_provider"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_AiRequestModel(UniversalBaseModel):
    field: typing.Literal["ai_request_model"] = "ai_request_model"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_AiResponseModel(UniversalBaseModel):
    field: typing.Literal["ai_response_model"] = "ai_response_model"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_Api(UniversalBaseModel):
    field: typing.Literal["api"] = "api"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_ApiProduct(UniversalBaseModel):
    field: typing.Literal["api_product"] = "api_product"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_ApiProductVersion(UniversalBaseModel):
    field: typing.Literal["api_product_version"] = "api_product_version"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_Application(UniversalBaseModel):
    field: typing.Literal["application"] = "application"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_Consumer(UniversalBaseModel):
    field: typing.Literal["consumer"] = "consumer"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[ScopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_ControlPlane(UniversalBaseModel):
    field: typing.Literal["control_plane"] = "control_plane"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_ControlPlaneGroup(UniversalBaseModel):
    field: typing.Literal["control_plane_group"] = "control_plane_group"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_DataPlaneNode(UniversalBaseModel):
    field: typing.Literal["data_plane_node"] = "data_plane_node"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[ScopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_DataPlaneNodeVersion(UniversalBaseModel):
    field: typing.Literal["data_plane_node_version"] = "data_plane_node_version"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_GatewayService(UniversalBaseModel):
    field: typing.Literal["gateway_service"] = "gateway_service"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[ScopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_LlmCacheStatus(UniversalBaseModel):
    field: typing.Literal["llm_cache_status"] = "llm_cache_status"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_LlmEmbeddingsModel(UniversalBaseModel):
    field: typing.Literal["llm_embeddings_model"] = "llm_embeddings_model"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_LlmEmbeddingsProvider(UniversalBaseModel):
    field: typing.Literal["llm_embeddings_provider"] = "llm_embeddings_provider"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_Portal(UniversalBaseModel):
    field: typing.Literal["portal"] = "portal"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_Realm(UniversalBaseModel):
    field: typing.Literal["realm"] = "realm"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_ResponseSource(UniversalBaseModel):
    field: typing.Literal["response_source"] = "response_source"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_Route(UniversalBaseModel):
    field: typing.Literal["route"] = "route"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[ScopedUuid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_StatusCode(UniversalBaseModel):
    field: typing.Literal["status_code"] = "status_code"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_StatusCodeGrouped(UniversalBaseModel):
    field: typing.Literal["status_code_grouped"] = "status_code_grouped"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_UpstreamStatusCode(UniversalBaseModel):
    field: typing.Literal["upstream_status_code"] = "upstream_status_code"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllFilterItems_UpstreamStatusCodeGrouped(UniversalBaseModel):
    field: typing.Literal["upstream_status_code_grouped"] = "upstream_status_code_grouped"
    operator: RequestsFilterType
    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AllFilterItems = typing_extensions.Annotated[
    typing.Union[
        AllFilterItems_AiPlugin,
        AllFilterItems_AiProvider,
        AllFilterItems_AiRequestModel,
        AllFilterItems_AiResponseModel,
        AllFilterItems_Api,
        AllFilterItems_ApiProduct,
        AllFilterItems_ApiProductVersion,
        AllFilterItems_Application,
        AllFilterItems_Consumer,
        AllFilterItems_ControlPlane,
        AllFilterItems_ControlPlaneGroup,
        AllFilterItems_DataPlaneNode,
        AllFilterItems_DataPlaneNodeVersion,
        AllFilterItems_GatewayService,
        AllFilterItems_LlmCacheStatus,
        AllFilterItems_LlmEmbeddingsModel,
        AllFilterItems_LlmEmbeddingsProvider,
        AllFilterItems_Portal,
        AllFilterItems_Realm,
        AllFilterItems_ResponseSource,
        AllFilterItems_Route,
        AllFilterItems_StatusCode,
        AllFilterItems_StatusCodeGrouped,
        AllFilterItems_UpstreamStatusCode,
        AllFilterItems_UpstreamStatusCodeGrouped,
    ],
    pydantic.Field(discriminator="field"),
]
