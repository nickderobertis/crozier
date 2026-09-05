

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CodeBundleLocationSandboxSandboxSpec_Modal(UniversalBaseModel):
    provider: typing.Literal["modal"] = "modal"
    snapshot_ref: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CodeBundleLocationSandboxSandboxSpec_Lambda(UniversalBaseModel):
    provider: typing.Literal["lambda"] = "lambda"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CodeBundleLocationSandboxSandboxSpec = typing_extensions.Annotated[
    typing.Union[CodeBundleLocationSandboxSandboxSpec_Modal, CodeBundleLocationSandboxSandboxSpec_Lambda],
    pydantic.Field(discriminator="provider"),
]
