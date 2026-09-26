

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_None(
    UniversalBaseModel
):
    type: typing.Literal["none"] = "none"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_Tcp(
    UniversalBaseModel
):
    type: typing.Literal["tcp"] = "tcp"
    host: str
    port: int
    timeout_ms: typing_extensions.Annotated[int, FieldMetadata(alias="timeoutMs"), pydantic.Field(alias="timeoutMs")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_Http(
    UniversalBaseModel
):
    type: typing.Literal["http"] = "http"
    url: str
    expected_status: typing_extensions.Annotated[
        int, FieldMetadata(alias="expectedStatus"), pydantic.Field(alias="expectedStatus")
    ]
    timeout_ms: typing_extensions.Annotated[int, FieldMetadata(alias="timeoutMs"), pydantic.Field(alias="timeoutMs")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_Ws(
    UniversalBaseModel
):
    type: typing.Literal["ws"] = "ws"
    url: str
    timeout_ms: typing_extensions.Annotated[int, FieldMetadata(alias="timeoutMs"), pydantic.Field(alias="timeoutMs")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness = (
    typing_extensions.Annotated[
        typing.Union[
            PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_None,
            PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_Tcp,
            PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_Http,
            PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness_Ws,
        ],
        pydantic.Field(discriminator="type"),
    ]
)
