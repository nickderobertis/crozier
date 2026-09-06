

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_bundle_location_experiment_position import CodeBundleLocationExperimentPosition


class CodeBundleLocationExperiment(UniversalBaseModel):
    eval_name: str
    position: CodeBundleLocationExperimentPosition

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
