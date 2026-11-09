

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .requests_filter_type import RequestsFilterType
from .scoped_uuid import ScopedUuid
from .unscoped_uuid import UnscopedUuid


class LlmFiltersItem_AiPlugin(UniversalBaseModel):
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


class LlmFiltersItem_AiProvider(UniversalBaseModel):
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


class LlmFiltersItem_AiRequestModel(UniversalBaseModel):
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


class LlmFiltersItem_AiResponseModel(UniversalBaseModel):
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


class LlmFiltersItem_Application(UniversalBaseModel):
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


class LlmFiltersItem_Consumer(UniversalBaseModel):
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


class LlmFiltersItem_ControlPlane(UniversalBaseModel):
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


class LlmFiltersItem_ControlPlaneGroup(UniversalBaseModel):
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


class LlmFiltersItem_GatewayService(UniversalBaseModel):
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


class LlmFiltersItem_LlmCacheStatus(UniversalBaseModel):
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


class LlmFiltersItem_LlmEmbeddingsModel(UniversalBaseModel):
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


class LlmFiltersItem_LlmEmbeddingsProvider(UniversalBaseModel):
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


class LlmFiltersItem_Realm(UniversalBaseModel):
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


class LlmFiltersItem_Route(UniversalBaseModel):
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


class LlmFiltersItem_StatusCode(UniversalBaseModel):
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


class LlmFiltersItem_StatusCodeGrouped(UniversalBaseModel):
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


LlmFiltersItem = typing_extensions.Annotated[
    typing.Union[
        LlmFiltersItem_AiPlugin,
        LlmFiltersItem_AiProvider,
        LlmFiltersItem_AiRequestModel,
        LlmFiltersItem_AiResponseModel,
        LlmFiltersItem_Application,
        LlmFiltersItem_Consumer,
        LlmFiltersItem_ControlPlane,
        LlmFiltersItem_ControlPlaneGroup,
        LlmFiltersItem_GatewayService,
        LlmFiltersItem_LlmCacheStatus,
        LlmFiltersItem_LlmEmbeddingsModel,
        LlmFiltersItem_LlmEmbeddingsProvider,
        LlmFiltersItem_Realm,
        LlmFiltersItem_Route,
        LlmFiltersItem_StatusCode,
        LlmFiltersItem_StatusCodeGrouped,
    ],
    pydantic.Field(discriminator="field"),
]
