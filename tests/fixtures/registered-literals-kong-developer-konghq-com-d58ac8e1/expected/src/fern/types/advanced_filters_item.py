

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .requests_filter_type import RequestsFilterType
from .scoped_uuid import ScopedUuid
from .unscoped_uuid import UnscopedUuid


class AdvancedFiltersItem_Api(UniversalBaseModel):
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


class AdvancedFiltersItem_ApiProduct(UniversalBaseModel):
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


class AdvancedFiltersItem_ApiProductVersion(UniversalBaseModel):
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


class AdvancedFiltersItem_Application(UniversalBaseModel):
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


class AdvancedFiltersItem_Consumer(UniversalBaseModel):
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


class AdvancedFiltersItem_ControlPlane(UniversalBaseModel):
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


class AdvancedFiltersItem_ControlPlaneGroup(UniversalBaseModel):
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


class AdvancedFiltersItem_DataPlaneNode(UniversalBaseModel):
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


class AdvancedFiltersItem_DataPlaneNodeVersion(UniversalBaseModel):
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


class AdvancedFiltersItem_GatewayService(UniversalBaseModel):
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


class AdvancedFiltersItem_Portal(UniversalBaseModel):
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


class AdvancedFiltersItem_Realm(UniversalBaseModel):
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


class AdvancedFiltersItem_ResponseSource(UniversalBaseModel):
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


class AdvancedFiltersItem_Route(UniversalBaseModel):
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


class AdvancedFiltersItem_StatusCode(UniversalBaseModel):
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


class AdvancedFiltersItem_StatusCodeGrouped(UniversalBaseModel):
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


class AdvancedFiltersItem_UpstreamStatusCode(UniversalBaseModel):
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


class AdvancedFiltersItem_UpstreamStatusCodeGrouped(UniversalBaseModel):
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


AdvancedFiltersItem = typing_extensions.Annotated[
    typing.Union[
        AdvancedFiltersItem_Api,
        AdvancedFiltersItem_ApiProduct,
        AdvancedFiltersItem_ApiProductVersion,
        AdvancedFiltersItem_Application,
        AdvancedFiltersItem_Consumer,
        AdvancedFiltersItem_ControlPlane,
        AdvancedFiltersItem_ControlPlaneGroup,
        AdvancedFiltersItem_DataPlaneNode,
        AdvancedFiltersItem_DataPlaneNodeVersion,
        AdvancedFiltersItem_GatewayService,
        AdvancedFiltersItem_Portal,
        AdvancedFiltersItem_Realm,
        AdvancedFiltersItem_ResponseSource,
        AdvancedFiltersItem_Route,
        AdvancedFiltersItem_StatusCode,
        AdvancedFiltersItem_StatusCodeGrouped,
        AdvancedFiltersItem_UpstreamStatusCode,
        AdvancedFiltersItem_UpstreamStatusCodeGrouped,
    ],
    pydantic.Field(discriminator="field"),
]
