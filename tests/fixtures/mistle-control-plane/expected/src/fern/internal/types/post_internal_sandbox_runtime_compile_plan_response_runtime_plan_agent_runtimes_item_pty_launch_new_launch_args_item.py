

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunchArgsItem_Literal(
    UniversalBaseModel
):
    kind: typing.Literal["literal"] = "literal"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunchArgsItem_ThreadId(
    UniversalBaseModel
):
    kind: typing.Literal["threadId"] = "threadId"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunchArgsItem = typing_extensions.Annotated[
    typing.Union[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunchArgsItem_Literal,
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunchArgsItem_ThreadId,
    ],
    pydantic.Field(discriminator="kind"),
]
