

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CodeBundleLocationExperimentPosition_Task(UniversalBaseModel):
    type: typing.Literal["task"] = "task"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CodeBundleLocationExperimentPosition_Scorer(UniversalBaseModel):
    type: typing.Literal["scorer"] = "scorer"
    index: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CodeBundleLocationExperimentPosition = typing_extensions.Annotated[
    typing.Union[CodeBundleLocationExperimentPosition_Task, CodeBundleLocationExperimentPosition_Scorer],
    pydantic.Field(discriminator="type"),
]
