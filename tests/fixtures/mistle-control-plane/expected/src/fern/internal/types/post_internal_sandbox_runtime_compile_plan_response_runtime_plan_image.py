

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanImage_Base(UniversalBaseModel):
    source: typing.Literal["base"] = "base"
    image_ref: typing_extensions.Annotated[str, FieldMetadata(alias="imageRef"), pydantic.Field(alias="imageRef")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanImage_Snapshot(UniversalBaseModel):
    source: typing.Literal["snapshot"] = "snapshot"
    image_ref: typing_extensions.Annotated[str, FieldMetadata(alias="imageRef"), pydantic.Field(alias="imageRef")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanImage = typing_extensions.Annotated[
    typing.Union[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanImage_Base,
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanImage_Snapshot,
    ],
    pydantic.Field(discriminator="source"),
]
