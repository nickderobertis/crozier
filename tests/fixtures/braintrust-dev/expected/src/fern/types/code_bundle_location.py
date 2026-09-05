

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_bundle_location_experiment_position import CodeBundleLocationExperimentPosition
from .code_bundle_location_sandbox_sandbox_spec import CodeBundleLocationSandboxSandboxSpec


class CodeBundleLocation_Experiment(UniversalBaseModel):
    type: typing.Literal["experiment"] = "experiment"
    eval_name: str
    position: CodeBundleLocationExperimentPosition

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CodeBundleLocation_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    index: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CodeBundleLocation_Sandbox(UniversalBaseModel):
    type: typing.Literal["sandbox"] = "sandbox"
    sandbox_spec: CodeBundleLocationSandboxSandboxSpec
    entrypoints: typing.Optional[typing.List[str]] = None
    eval_name: str
    parameters: typing.Optional[typing.Dict[str, typing.Any]] = None
    evaluator_definition: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CodeBundleLocation = typing_extensions.Annotated[
    typing.Union[CodeBundleLocation_Experiment, CodeBundleLocation_Function, CodeBundleLocation_Sandbox],
    pydantic.Field(discriminator="type"),
]
