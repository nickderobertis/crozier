

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1workflow_stage import V1Alpha1WorkflowStage


class V1Alpha1WorkflowResourceSpec(UniversalBaseModel):
    stages: typing.List[V1Alpha1WorkflowStage]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
