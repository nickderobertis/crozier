

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Bearer(UniversalBaseModel):
    type: typing.Literal["bearer"] = "bearer"
    target: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Basic(UniversalBaseModel):
    type: typing.Literal["basic"] = "basic"
    target: str
    username: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Header(UniversalBaseModel):
    type: typing.Literal["header"] = "header"
    target: str
    credential_prefix: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="credentialPrefix"), pydantic.Field(alias="credentialPrefix")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Query(UniversalBaseModel):
    type: typing.Literal["query"] = "query"
    target: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_PathSegmentPrefix(
    UniversalBaseModel
):
    type: typing.Literal["path_segment_prefix"] = "path_segment_prefix"
    segment_prefix: typing_extensions.Annotated[
        str, FieldMetadata(alias="segmentPrefix"), pydantic.Field(alias="segmentPrefix")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_AwsSigv4(
    UniversalBaseModel
):
    type: typing.Literal["aws_sigv4"] = "aws_sigv4"
    service: str
    region: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection = typing_extensions.Annotated[
    typing.Union[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Bearer,
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Basic,
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Header,
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_Query,
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_PathSegmentPrefix,
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection_AwsSigv4,
    ],
    pydantic.Field(discriminator="type"),
]
